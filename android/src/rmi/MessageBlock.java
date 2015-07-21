package rmi;

import java.util.HashMap;
import java.util.Map;

public class MessageBlock {
	public static abstract class MessageBase
	{
		public abstract void __read(Serializer __is);
		public abstract void __write(Serializer __os);
	}
	
	public static abstract class AutoRegist
	{
		public abstract MessageBase create();
	}
	
	private static Map<String, AutoRegist> _mapClass;
	static{
		_mapClass = new HashMap<String, AutoRegist>();
	}
	
	public static void regist(String name, AutoRegist autoRegist)
	{
		_mapClass.put(name, autoRegist);
	}
	
	private int __command;
	private MessageBase __messageBase;
	
	public MessageBlock()
	{
		__command = 0;
		__messageBase = null;
	}
	
	public MessageBlock(Serializer __is)
	{
		__command = __is.readInt();
		
		int size = __is.readInt();
		for (int i = 0; i < size; ++i)
		{
			__is.readInt();
		}
		
		String msgName = __is.readString();
		AutoRegist autoRegist = _mapClass.get(msgName);
		if (null != autoRegist)
		{
			__messageBase = autoRegist.create();
		}
		else
		{
			Logger.log("Message " + msgName + " not registered.");
		}
	}
	
	public int getCommand()
	{
		return __command;
	}
	
	public MessageBase getMessageBase()
	{
		return __messageBase;
	}
}
