package rmi;

import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class ProxyManager {
	private Map<String, RmiCore.RmiProxyBase> _mapProxy;
	private static ProxyManager _inst = null;
	
	private ProxyManager()
	{
		_mapProxy = new HashMap<String, RmiCore.RmiProxyBase>();
	}
	
	public ProxyManager instance()
	{
		if (_inst == null)
		{
			_inst = new ProxyManager();
		}
		
		return _inst;
	}
	
	public void addProxy(RmiCore.RmiProxyBase proxy)
	{
		_mapProxy.put(proxy.getName(), proxy);
	}
	
	public RmiCore.RmiProxyBase getProxy(String name)
	{
		return _mapProxy.get(name);
	}
}
