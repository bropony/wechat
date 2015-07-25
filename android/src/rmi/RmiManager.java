package rmi;

import rmi.Logger;
import rmi.RmiClient;

import java.net.URI;
import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;


public class RmiManager implements Runnable{
	final public static Integer ClientType_LoginManager = new Integer(1); //登录服务器
	final public static Integer ClientType_GateServer = new Integer(2);   //业务服务器
	
	static private RmiManager _inst = null;
	static private Thread _timer = null;
	static private Object _lock = new Object();
	
	private long _rmiTimeout;
	boolean _isStopped;
	
	private Map<Integer, RmiClient> _mapClient;
	
	static public RmiManager instance(){
		if (_inst == null)
		{
			_inst = new RmiManager();
		}
		
		return _inst;
	}
	
	private RmiManager(){
		_rmiTimeout = 0;
		_mapClient = new HashMap<Integer, RmiClient>();
		_timer = new Thread(this);
		
		_isStopped = false;
	}
	
	public void startService()
	{
		_timer.start();
	}
	
	public void stopService()
	{
		_isStopped = true;
	}
	
	
	public void addRmiClient(Integer clientType, URI clientURI)
	{
		RmiClient client = new RmiClient(clientURI);
		addRmiClient(clientType, client);
	}
	
	public void addRmiClient(Integer clientType, RmiClient client)
	{
		synchronized (_lock)
		{
			_mapClient.put(clientType, client);	
		}
	}
	
	public RmiClient getRmiClient(Integer clientType)
	{
		return _mapClient.get(clientType);
	}
	
	public void setRmiTimeout(long timeout){
		if (timeout > 300){
			_rmiTimeout = timeout;
		}
	}
	
	private void __sendOut(){
		if (_mapClient.size() <= 0)
		{
			return;
		}
		
		Date now = new Date();
		
		synchronized (_lock)
		{
			Set<Integer> keySet = _mapClient.keySet();
			Iterator<Integer> it = keySet.iterator();
			while (it.hasNext())
			{
				Integer key = it.next();
				RmiClient client = _mapClient.get(key);
				client.__sendOut(_rmiTimeout, now);
			}	
		}
	}
	
	@Override
	public void run(){
		while(true){
			
			if (_isStopped)
			{
				break;
			}
			
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

