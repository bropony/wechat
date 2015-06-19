#ifndef __GAMIT_MESSAGE_MESSAHGE_HANDLER_H__
#define __GAMIT_MESSAGE_MESSAHGE_HANDLER_H__

#include <gamit/message/Message.h>

namespace gamit
{
	class CMessageHandlerBase
	{
	public:
		virtual void onMessage(const MessageBlockPtr & msgBlock) = 0;
	};
	typedef std::CSharedPtr<CMessageHandlerBase> CMessageHandlerBasePtr;
	typedef std::map<int, CMessageHandlerBasePtr> MapMessageHandlerBase;
}

#endif