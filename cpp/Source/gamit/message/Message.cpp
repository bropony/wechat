#include "Message.h"

using namespace gamit;

MessageBlock::MapCreateFunc MessageBlock::_mapCreateFunc;

MessageBlock::MessageBlock(CSerializer & __is)
:_command()
,_messageBase()
, __os()
{
	__is.read(_command);

	int size = 0;
	__is.read(size);

	// toIdList
	for (int i = 0; i < size; i++)
	{
		int dummy = 0;
		__is.read(dummy);
	}

	std::string msgName;
	__is.read(msgName);

	_messageBase = createMessageBase(msgName);
	if (nullptr != _messageBase)
	{
		_messageBase->__read(__is);
	}
}

MessageBlock::MessageBlock(int command, const MessageBasePtr & msgBase)
:_command(command)
,_messageBase(msgBase)
,__os()
{
	__os.startToWrite();
	__os.write(byte_t(ERmiType::MessageBlock));
	__os.write(_command);
	__os.write(int(0)); //no toIdList
	__os.write(_messageBase->__name());

	if (nullptr != _messageBase)
	{
		_messageBase->__write(__os);
	}
}

const std::string & MessageBlock::getBuffer()
{
	return __os.getBuffer();
}

MessageBasePtr MessageBlock::createMessageBase(const std::string & msgName)
{
	auto found = _mapCreateFunc.find(msgName);

	if (found == _mapCreateFunc.end())
	{
		return nullptr;
	}

	return found->second();
}

void MessageBlock::registCreateFunc(const std::string & msgName, CreateFunc func)
{
	_mapCreateFunc[msgName] = func;
}
