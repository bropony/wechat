#ifndef	__GAMIT_WEBSOCKET_CONNECTOR_BASE_H__
#define __GAMIT_WEBSOCKET_CONNECTOR_BASE_H__

#include <gamit/rmi/RmiCore.h>

namespace gamit
{
	class CConnectorBase
	{
	public:
		virtual ~CConnectorBase(){}

		virtual void onConnected() = 0;
		virtual void onOpen() = 0;
		virtual void onMessage(const std::string & payload, bool isBinary) = 0;
		virtual void send(const std::string & payload, bool isBinary) = 0;

		virtual void start() = 0;
		virtual void stop() = 0;

		void setRmiClient(const CRmiClientBasePtr & client)
		{
			_client = client;
		}

	protected:
		CRmiClientBasePtr _client;
	};
	typedef std::CSharedPtr<CConnectorBase> CConnectorBasePtr;
}

#endif