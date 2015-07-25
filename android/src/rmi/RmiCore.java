package rmi;

import java.util.Date;

public class RmiCore {
	public static abstract class RmiResponseBase
	{
		private int __msgId;
		private Date __createDt;
		
		public RmiResponseBase()
		{
			__msgId = 0;
			__createDt = new Date();
		}
		
		public void setMsgId(int msgId)
		{
			this.__msgId = msgId;
		}
		
		public int getMsgId()
		{
			return __msgId;
		}
		
		public boolean isExpired(Date now, long timeout)
		{
			if (timeout <= 0)
			{
				return false;
			}
			
			if ((now.getTime() - __createDt.getTime()) > timeout){
				return true;
			}
			
			return false;
		}
		
		public abstract void __onResponse(Serializer __is);
		public abstract void __onError(String what, int code);
		public abstract void __onTimeout();
	}
	
	public static class RmiProxyBase
	{
		private String __name;
		protected RmiClient _rmiClient;
		
		public RmiProxyBase(String name)
		{
			__name = name;
			_rmiClient = null;
		}
		
		public String getName()
		{
			return __name;
		}
		
		public void setRmiClient(RmiClient client)
		{
			_rmiClient = client;
		}
		
		public void call(Serializer __os, RmiResponseBase resposne)
		{
			if (_rmiClient != null)
			{
				_rmiClient.invoke(resposne, __os);
			}
			else
			{
				Logger.log("RmiClient not set for Proxy: " + __name);
			}
		}
	}
}
