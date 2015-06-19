#ifndef __GAMIT_RMI_RMI_CLIENT_H__
#define __GAMIT_RMI_RMI_CLIENT_H__

#include <gamit/serialize/serializer.h>
#include <gamit/util/sharedptr.h>
#include <gamit/rmi/RmiCore.h>
#include <map>

#include <gamit/net/websocket/WebsocketConnector.h>

namespace gamit
{
	class CRmiClient : public CRmiClientBase
	{
	public:
		CRmiClient(int channelType, const std::string & ip, int port, long64_t callbackTimeout = 30);

		virtual void onOpen();
		virtual void onClose();
		virtual void onMessage(const std::string & payload, bool isBinary);
		virtual void send(const CSerializer & __os);
		virtual void send(const std::string & payload, bool isBinary);

		virtual void start();
		virtual void stop();

		virtual void addResponse(const CRmiResponseBasePtr & cb);

	private:
		void onResponse(CSerializer & __is);
		void onError(CSerializer & __is);
		void onMessage(CSerializer & __is);
		void onTimeout();

	private:
		typedef std::map<std::string, CRmiProxyBasePtr> MapProxy;
		typedef std::map<int, CRmiResponseBasePtr> MapResponse;

		int _channelType;
		MapProxy _mapProxy;
		MapResponse _mapResponse;
		long64_t _callbackTimeout; // mills

		CConnectorBasePtr _connector;
	};
}

#endif