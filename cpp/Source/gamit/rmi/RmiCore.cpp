#include <gamit/rmi/RmiCore.h>

int gamit::CRmiProxyBase::_msgIdBase = 0;

void gamit::CRmiClientBase::onOpen()
{
	if (_connectionOpenCallback != nullptr)
	{
		_connectionOpenCallback->onOpen();
	}
}

void gamit::CRmiClientBase::onClose()
{

}

void gamit::CRmiClientBase::setConnectionOpenCallback(const CConnectionOpenCallbackBasePtr & callback)
{
	_connectionOpenCallback = callback;
}

gamit::CRmiResponseBase::CRmiResponseBase()
:_msgId()
,_createDt()
{
}

void gamit::CRmiResponseBase::setMsgId(int msgId)
{ 
	_msgId = msgId; 
}
int gamit::CRmiResponseBase::getMsgId()
{ 
	return _msgId;
}

bool gamit::CRmiResponseBase::isExpired(long64_t mills)
{
	gamit::CDateTime now;

	long64_t passedMills = (now - _createDt).getTotalMills();
	if (passedMills >= mills)
	{
		return true;
	}

	return false;
}

void gamit::CRmiProxyBase::invoke(CSerializer & __os, const CRmiResponseBasePtr & __cb)
{
	if (_client != nullptr)
	{
		_client->send(__os);
		_client->addResponse(__cb);
	}
}

void gamit::CRmiProxyBase::setClient(const CRmiClientBasePtr & client)
{
	_client = client;
}

int gamit::CRmiProxyBase::__getMsgId()
{
	_msgIdBase += 1;
	return _msgIdBase;
}
