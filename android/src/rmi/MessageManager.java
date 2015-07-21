package rmi;

import java.util.HashMap;
import java.util.Map;

public class MessageManager {
	private Map<Integer, MessageHandler> _mapHandler;
	
	static MessageManager _inst;
	static {
		_inst = new MessageManager();
	}
	
	private MessageManager()
	{
		_mapHandler = new HashMap<Integer, MessageHandler>();
	}
	
	public static MessageManager instance()
	{
		return _inst;
	}
	
	public void registMessageHandler(int command, MessageHandler handler)
	{
		_mapHandler.put(new Integer(command), handler);
	}
	
	public void onMessage(Serializer __is)
	{
		MessageBlock msgBlock = new MessageBlock(__is);
		int command = msgBlock.getCommand();
		Integer key = new Integer(command);
		
		MessageHandler handler = _mapHandler.get(key);
		if (handler != null)
		{
			handler.onMessage(msgBlock);
		}
	}
}
