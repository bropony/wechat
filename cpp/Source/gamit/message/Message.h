#ifndef __GAMIT_MESSAGE_MESSAGE_H__
#define __GAMIT_MESSAGE_MESSAGE_H__

#include "gamit/serialize/serializer.h"
#include "gamit/util/sharedptr.h"
#include <functional>
#include <map>

namespace gamit
{
	class MessageBase
	{
	public:
		virtual void __read(CSerializer & __is) = 0;
		virtual void __write(CSerializer & __os) const = 0;
		virtual const std::string & __name() const = 0;

		virtual ~MessageBase(){}
	};
	typedef std::CSharedPtr<MessageBase> MessageBasePtr;
	typedef std::function<MessageBasePtr()> CreateFunc;

	class MessageBlock
	{
	public:
		MessageBlock(CSerializer & __is);
		MessageBlock(int command, const MessageBasePtr & msgBase);

		const std::string & getBuffer();

	public:
		static MessageBasePtr createMessageBase(const std::string & msgName);
		static void registCreateFunc(const std::string & msgName, CreateFunc func);

	public:
		typedef std::map<std::string, CreateFunc> MapCreateFunc;

		int _command;
		MessageBasePtr _messageBase;
		CSerializer __os;

		static MapCreateFunc _mapCreateFunc;
	};
	typedef std::CSharedPtr<MessageBlock> MessageBlockPtr;
}

#endif