package rmi;

import rmi.Logger;
import rmi.Serializer;
import rmi.RmiCore;
import rmi.RmiCore.RmiProxyBase;

import java.net.URI;
import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import org.java_websocket.client.WebSocketClient;
import org.java_websocket.framing.Framedata;
import org.java_websocket.handshake.ServerHandshake;

class WebSocketClientImpl extends WebSocketClient{ 
	private RmiClient _rmiClient;
	
	public WebSocketClientImpl(URI serverURI, RmiClient rmiClient) {
		super(serverURI);
		_rmiClient = rmiClient;
	}

	@Override
	public void onOpen(ServerHandshake handshakedata) {
		_rmiClient.onOpen(handshakedata);
	}

	@Override
	public void onMessage(String message) {
		_rmiClient.onMessage(message);
	}
	
	@Override
	public void onMessage( ByteBuffer bytes ) {
		_rmiClient.onMessage(bytes);
	}
	
	@Override
	public void onFragment( Framedata frame ) {
		_rmiClient.onFragment(frame);
	}

	@Override
	public void onClose(int code, String reason, boolean remote) {
		_rmiClient.onClose(code, reason, remote);
	}

	@Override
	public void onError(Exception ex) {
		_rmiClient.onError(ex);
	}
}


public class RmiClient{
	private static Object _lock = new Object();
	
	private WebSocketClient _ws;
	private URI _serverURI;
	boolean _isClosedByError;
	
	private Map<Integer, RmiCore.RmiResponseBase> _mapCallback;
	private ArrayList<Serializer> _outgoings;
	
	public RmiClient(URI serverURI){

		_serverURI = serverURI;
		_ws = null;
		_isClosedByError = false;
		
		_mapCallback = new HashMap<Integer, RmiCore.RmiResponseBase>();
		_outgoings = new ArrayList<Serializer>();

	}
	
	/*
	 * @brief -- Connect to Server
	 * It will give up connection try if the connection is closed by the Server OR
	 * some ERROR has occurred.
	 * If you still want to setup a connection, use the forceConnect() method
	 */
	public void connect(){
		if (_isClosedByError)
		{
			Logger.log("Error Occured. Obort connectio request to " + _serverURI.toString());
			return;
		}
		
		if (_ws == null || _ws.isClosed() || _ws.isFlushAndClose())
		{
			Logger.log("Connecting to Server: " + _serverURI.toString());
			
			_isClosedByError = false;
			_ws = new WebSocketClientImpl(_serverURI, this);
			_ws.connect();
		}
	}
	
	/*
	 * @brief -- Forcedly try connecting to the Server.
	 */
	public void forceConnect()
	{
		_isClosedByError = false;
		
		this.connect();
	}
	
	/*
	 * @brief -- Close a connection manually if it is on longer used.
	 * A connection can be setup again simply by calling connect()
	 */
	public void closeConnection()
	{
		this._ws.close();
		this._ws = null;
	}
	
	public void bindProxy(String name)
	{
		RmiProxyBase proxy = ProxyManager.instance().getProxy(name);
		if (proxy != null)
		{
			proxy.setRmiClient(this);
		}
		else
		{
			Logger.log("RmiClient.bindProxy: not such proxy: ", name);
		}
	}

	
	//
	public void onOpen(ServerHandshake handshakedata) {
		Logger.log("onOpen", "Net connection opened");
	}

	public void onMessage(String message) {
		Serializer __is = new Serializer(message.getBytes());
		onMessage(__is);
	}
	
	public void onMessage( ByteBuffer bytes ) {
		Serializer __is = new Serializer(bytes);
		onMessage(__is);
	}
	
	public void onFragment( Framedata frame ) {
		Serializer __is = new Serializer(frame.getPayloadData());
		onMessage(__is);
	}
	
	public void onMessage(Serializer __is){
		__is.simpleDecrypt();
		__is.startToRead();
		
		byte rmiType = __is.readByte();
		
		switch (rmiType)
		{
		case Serializer.RmiDataResponse:
			__onResponse(__is);
			break;
		case Serializer.RmiDataException:
			__onError(__is);
			break;
		case Serializer.RmiDataMessageBlock:
			__onRmiMessage(__is);
			break;
		default:
			Logger.log("Unknow RmiType");
			break;
		}
	}
	
	private void __onResponse(Serializer __is)
	{
		int msgId = __is.readInt();
		Integer key = new Integer(msgId);
		RmiCore.RmiResponseBase response = _mapCallback.get(key);
		
		if (null != response)
		{
			response.__onResponse(__is);
			
			_mapCallback.remove(key);
		}
	}
	
	private void __onError(Serializer __is)
	{
		int msgId = __is.readInt();
		Integer key = new Integer(msgId);
		
		String what = __is.readString();
		int code = __is.readInt();
		
		RmiCore.RmiResponseBase response = _mapCallback.get(key);
		if (null != response)
		{
			response.__onError(what, code);
			
			_mapCallback.remove(key);
		}
	}
	
	private void __onRmiMessage(Serializer __is)
	{
		MessageManager.instance().onMessage(__is);
	}

	public void onClose(int code, String reason, boolean remote) {
		String __log = "" + code + ", " + reason + ", " + remote;
		Logger.log("onClose", __log);
		
		_isClosedByError = true;
	}

	public void onError(Exception ex) {
		Logger.log("onError", ex.toString());
		
		_isClosedByError = true;
	}
	
	public void invoke(RmiCore.RmiResponseBase __cb, Serializer __os){
		synchronized(_lock){
			__os.simpleEncrypt();
			
			_outgoings.add(__os);
			Integer key = new Integer(__cb.getMsgId());
			
			_mapCallback.put(key, __cb);
		}
	}
	
	public void __sendOut(long rmiTimeout, Date sinceDt){
		if (this._outgoings.size() <= 0){
			return;
		}
		
		if (this._ws == null){
			this.connect();
			return;
		}
		
		while (_outgoings.size() > 0){
			if (!this._ws.isOpen()){
				
				if (this._ws.isConnecting())
				{
					System.out.println("Connecting to Server");
				}
				
				if (this._ws.isClosed() || this._ws.isFlushAndClose())
				{
					System.out.println("Reconnect to Server");
					this.connect();
				}
				
				break;
			}
			
			synchronized(_lock){
				Serializer og = _outgoings.get(0);
				this._ws.send(og.getBytes());
				_outgoings.remove(0);
			}
		}
		
		synchronized(_lock){
			Set<Integer> keySet = null;
			
			keySet = _mapCallback.keySet();			
			Iterator<Integer> it = keySet.iterator();
			while (it.hasNext())
			{
				Integer key = it.next();
				
				RmiCore.RmiResponseBase cb = _mapCallback.get(key);
				if (null == cb)
				{
					continue;
				}
					
				if (cb.isExpired(sinceDt, rmiTimeout))
				{
					cb.__onTimeout();
					_mapCallback.remove(key);
				}
			}
		}
	}
}

