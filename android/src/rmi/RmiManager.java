package rmi;

import rmi.Logger;
import rmi.Serializer;
import rmi.RmiCore;

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
	public WebSocketClientImpl(URI serverURI) {
		super(serverURI);
	}

	@Override
	public void onOpen(ServerHandshake handshakedata) {
		RmiManager.instance().onOpen(handshakedata);
	}

	@Override
	public void onMessage(String message) {
		RmiManager.instance().onMessage(message);
	}
	
	@Override
	public void onMessage( ByteBuffer bytes ) {
		RmiManager.instance().onMessage(bytes);
	}
	
	@Override
	public void onFragment( Framedata frame ) {
		RmiManager.instance().onFragment(frame);
	}

	@Override
	public void onClose(int code, String reason, boolean remote) {
		RmiManager.instance().onClose(code, reason, remote);
	}

	@Override
	public void onError(Exception ex) {
		RmiManager.instance().onError(ex);
	}
}


public class RmiManager implements Runnable{
	static private RmiManager _inst;
	static private Object _lock = new Object();
	static private Thread _timer;
	
	private long _rmiTimeout;
	private WebSocketClient _ws;
	private URI _serverURI;
	
	private Map<Integer, RmiCore.RmiResponseBase> _mapCallback;
	private ArrayList<Serializer> _outgoings;
	
	static public void initInstance(URI serverURI){
		if (null != _inst){
			return;
		}
		
		_inst = new RmiManager(serverURI);
		_timer.start();
	}
	
	static public RmiManager instance(){
		return _inst;
	}
	
	public RmiManager(URI serverURI){
		_rmiTimeout = 0;
		_serverURI = serverURI;
		_ws = null;
		
		_mapCallback = new HashMap<Integer, RmiCore.RmiResponseBase>();
		_outgoings = new ArrayList<Serializer>();
		
		_timer = new Thread(this);
	}
	
	public void setRmiTimeout(long timeout){
		if (timeout > 300){
			_rmiTimeout = timeout;
		}
	}
	
	public void connect(){
		if (_ws == null || _ws.isClosed() || _ws.isFlushAndClose())
		{
			_ws = new WebSocketClientImpl(_serverURI);
			_ws.connect();
		}
	}

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
	}

	public void onError(Exception ex) {
		Logger.log("onError", ex.toString());
	}
	
	public void invoke(RmiCore.RmiResponseBase __cb, Serializer __os){
		synchronized(_lock){
			__os.simpleEncrypt();
			
			_outgoings.add(__os);
			Integer key = new Integer(__cb.getMsgId());
			
			_mapCallback.put(key, __cb);
		}
	}
	
	private void __sendOut(){
		if (this._outgoings.size() <= 0){
			return;
		}
		
		if (this._ws == null){
			System.out.println("Connect to Server");
			
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
			Date now = new Date();
			
			Iterator<Integer> it = keySet.iterator();
			while (it.hasNext())
			{
				Integer key = it.next();
				
				RmiCore.RmiResponseBase cb = _mapCallback.get(key);
				if (null == cb)
				{
					continue;
				}
					
				if (cb.isExpired(now, _rmiTimeout))
				{
					cb.__onTimeout();
					_mapCallback.remove(key);
				}
			}
		}
	}
	
	@Override
	public void run(){
		while(true){
			try{
				Thread.sleep(30);
				__sendOut();
			}
			catch(InterruptedException e){
				Logger.log(e.toString());
			}
		}
	}
	
	public void join(){
		if (_timer != null && _timer.isAlive()){
			try{
				_timer.join();
			}
			catch(Exception e)
			{
				e.printStackTrace();
			}
		}
	}
}

