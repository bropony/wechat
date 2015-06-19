#include "MessageManager.h"

using namespace gamit;

CMessageManager * CMessageManager::_inst(nullptr);

CMessageManager::CMessageManager()
{

}

CMessageManager::~CMessageManager()
{

}


CMessageManager * CMessageManager::instance()
{
	if (nullptr == _inst)
	{
		_inst = new CMessageManager();
	}

	return _inst;
}

void CMessageManager::registHandler(int command, const CMessageHandlerBasePtr & handler)
{
	_mapMessageHandler[command] = handler;
}

void CMessageManager::__onMessage(CSerializer & __is)
{
	MessageBlockPtr msgBlock = new MessageBlock(__is);

	int command = msgBlock->_command;
	auto found = _mapMessageHandler.find(command);

	if (found != _mapMessageHandler.end())
	{
		found->second->onMessage(msgBlock);
	}
}

