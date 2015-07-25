import rmi.RmiManager;
import rmi.MessageManager;
import rmi.RmiClient;

import java.net.URI;

import message.MessageRegister;
import message.gate.*;

public class RmiSetting {
	public static void initSettings()
	{	
		RmiSetting.createGateServiceClient();
		RmiSetting.registMessageHandlers();
	}
	
	private static void createGateServiceClient()
	{
		URI serverURI = null;
		
		try{
			serverURI = new URI("ws://192.168.0.168:8001");
		}
		catch(Exception e)
		{
			e.printStackTrace();
			return;
		}
		
		RmiClient client = new RmiClient(serverURI);
		client.bindProxy("ITest");
		
		RmiManager.instance().addRmiClient(RmiManager.ClientType_GateServer, client);
		RmiSetting.bindGateServiceProxies(client);
	}
	
	private static void bindGateServiceProxies(RmiClient client)
	{
		client.bindProxy("ITest");
		
		// list more proxy bindings blow...
		// to do
	}
	
	private static void registMessageHandlers()
	{
		MessageManager.instance().registMessageHandler(command.ETestCommand.FirstMessage, new FirstMessageHandler());
		
		// list more handler registering blow...
		// to do
	}
}
