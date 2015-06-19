#include "WebsocketConnector.h"

#ifdef G_USE_WEBSOCKET

using namespace gamit;

CWebscocketConnctor::CWebscocketConnctor(const std::string & ip, int port)
:CConnectorBase()
{

}

void CWebscocketConnctor::onConnected()
{

}

void CWebscocketConnctor::onOpen()
{
	if (nullptr != _client)
	{
		_client->onOpen();
	}
}

void CWebscocketConnctor::onMessage(const std::string & payload, bool isBinary)
{
	if (nullptr != _client)
	{
		_client->onMessage(payload, isBinary);
	}
}

void CWebscocketConnctor::send(const std::string & payload, bool isBinary)
{

}

void CWebscocketConnctor::start()
{

}

void CWebscocketConnctor::stop()
{

}

#endif // G_USE_WEBSOCKET