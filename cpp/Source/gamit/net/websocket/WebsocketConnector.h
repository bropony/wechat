#ifndef __GAMIT_NET_WEBSOCKET_WEBSOCKET_CONNECTOR_H__
#define __GAMIT_NET_WEBSOCKET_WEBSOCKET_CONNECTOR_H__

#include <gamit/def/macros.h>
#include <gamit/net/ConnectorBase.h>

#ifdef G_USE_WEBSOCKET

namespace gamit
{
	class CWebscocketConnctor
		: public CConnectorBase
	{
	public:
		CWebscocketConnctor(const std::string & ip, int port);

		virtual void onConnected();
		virtual void onOpen();
		virtual void onMessage(const std::string & payload, bool isBinary);
		virtual void send(const std::string & payload, bool isBinary);

		virtual void start();
		virtual void stop();
	};
}

#endif // G_USE_WEBSOCKET

#endif // __GAMIT_NET_WEBSOCKET_WEBSOCKET_CONNECTOR_H__