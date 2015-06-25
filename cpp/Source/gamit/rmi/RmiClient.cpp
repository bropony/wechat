#include <rmi/RmiClient.h>
#include <message/MessageManager.h>
#include <gamit/util/logger.h>
#include <gamit/serialize/encrypt.h>

using namespace gamit;

CRmiClient::CRmiClient(int channelType, const std::string & ip, int port, long64_t callbackTimeout)
	:CRmiClientBase()
	,_channelType(channelType)
	,_mapProxy()
	,_mapResponse()
	,_callbackTimeout(callbackTimeout)
{
#ifdef G_USE_WEBSOCKET
	_connector = new CWebscocketConnctor(ip, port);
#elif G_USE_ASIO
	//_connector = new CAsioConnector(ip, prot);
#endif

	if (_callbackTimeout <= 0)
	{
		_callbackTimeout = 3600 * 1000; // on hour
	}
}

void CRmiClient::onOpen()
{
	CRmiClientBase::onOpen();
}

void CRmiClient::onClose()
{
	CRmiClientBase::onClose();
}

void CRmiClient::onMessage(const std::string & payload, bool isBinary)
{
	try{
		if (isBinary)
		{
			std::string decrypt = payload;
			CEncrypto::simpleDecrypt(decrypt);

			CSerializer __is(decrypt);
			__is.startToRead();
			byte_t __type = 0;
			__is.read(__type);

			if (__type <= 0 || __type > 4)
			{
				// not good
				return;
			}

			ERmiType rmiType = ERmiType(__type);

			switch (rmiType)
			{
			case gamit::ERmiType::RmiCall:
				// oops
				break;
			case gamit::ERmiType::RmiResponse:
				onResponse(__is);
				break;
			case gamit::ERmiType::MessageBlock:
				onMessage(__is);
				break;
			case gamit::ERmiType::RmiException:
				onError(__is);
				break;
			default:
				break;
			}
		}
		else
		{
			// todo
		}
	}
	catch (CException ex)
	{
		G_LOG_INFO("RmiError: [" << ex.what() << ", " << ex.code() << "]");
	}
}

void CRmiClient::start()
{
	_connector->start();
}

void CRmiClient::stop()
{
	_connector->stop();
}

void CRmiClient::addResponse(const CRmiResponseBasePtr & cb)
{
	_mapResponse[cb->getMsgId()] = cb;
}

void CRmiClient::send(const CSerializer & __os)
{
	send(__os.getBuffer(), true);
}

void CRmiClient::send(const std::string & payload, bool isBinary)
{
	std::string encrypt = payload;
	CEncrypto::simpleEncrypt(encrypt);

	_connector->send(encrypt, isBinary);
}

void CRmiClient::onResponse(CSerializer & __is)
{
	int __msgId = 0;
	__is.read(__msgId);

	auto found = _mapResponse.find(__msgId);
	if (found != _mapResponse.end())
	{
		found->second->__onResponse(__is);
		_mapResponse.erase(found);
	}
}

void CRmiClient::onError(CSerializer & __is)
{
	int __msgId = 0;
	__is.read(__msgId);

	auto found = _mapResponse.find(__msgId);
	if (found != _mapResponse.end())
	{
		found->second->__onError(__is);
		_mapResponse.erase(found);
	}
}

void CRmiClient::onMessage(CSerializer & __is)
{
	CMessageManager::instance()->__onMessage(__is);
}

void CRmiClient::onTimeout()
{
	MapResponse mapNotExpiredResponse;
	for (auto response : _mapResponse)
	{
		if (!response.second->isExpired(_callbackTimeout))
		{
			mapNotExpiredResponse.insert(response);
		}
		else
		{
			response.second->__onTimeout();
		}
	}

	if (mapNotExpiredResponse.size() != _mapResponse.size())
	{
		_mapResponse.swap(mapNotExpiredResponse);
	}
}
