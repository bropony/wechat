import java.net.URI;

import rmi.RmiManager;
import rmi.MessageManager;
import rmi.ProxyManager;
import rmi.RmiClient;
import rmi.MessageBlock;
import rmi.MessageHandler;
import message.MessageRegister;
import message.common.*;
import message.gate.*;

class FirstMessageHandler extends MessageHandler
{
	@Override
	public void onMessage(MessageBlock msgBlock)
	{
		gatemsg.SMessage msg = (gatemsg.SMessage)msgBlock.getMessageBase();
		
		System.out.println("onMessage: " + msg.var6 + ", " + msg.var7.toString());
	}
}

class ItestGetIntListResponse extends itest.ITest_getIntList_response
{
	public ItestGetIntListResponse()
	{
		super();
	}
	
	@Override
	public void onResponse(publicdef.SeqInt intList)
	{
		int[] data = intList.getArray();
		System.out.println("onResponse");
		
		for (int i : data)
		{
			System.out.print("" + i + " ");
		}
		System.out.println();
	}
	
	@Override
    public void onError(String what, int code)
    {
		System.out.println("onError. What: " + what + ", Code: " + code);
    }
    
	@Override
    public void onTimeout()
    {
    	System.out.println("Timeout...");
    }
}

public class RmiTest {
	public static void main(String[] argv)
	{
		MessageRegister.regist(); // always run before any settings...
		
		RmiSetting.initSettings();
		RmiManager.instance().startService();
		
		//a single RMI call TEST test...
		ItestGetIntListResponse response = new ItestGetIntListResponse();
		itest.ITestProxy proxy = (itest.ITestProxy)ProxyManager.instance().getProxy("ITest");
		proxy.getIntList(response, 10);
		
		RmiManager.instance().join();
		RmiManager.instance().stopService();
	}
}
