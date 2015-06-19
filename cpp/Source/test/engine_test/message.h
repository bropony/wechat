#ifndef __TEST_MESSAGE_H__
#define __TEST_MESSAGE_H__

#include "gamit/message/MessageManager.h"
#include "gamit/message/MessageHandler.h"

namespace Test
{
	class CMessageTest
	{
	public:
		static void runTest();
		
	private:
		static void resigt();
		static void send();
	};

	class CMsgHandler
		: public gamit::CMessageHandlerBase
	{
	public:
		virtual void onMessage(const gamit::MessageBlockPtr & msgBlock);
	};
	typedef std::CSharedPtr<CMsgHandler> CMsgHandlerPtr;
}

#endif