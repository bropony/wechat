#ifndef __GAMIT_MESSAGE_MESSAGE_MANAGER_H__
#define __GAMIT_MESSAGE_MESSAGE_MANAGER_H__

#include "gamit/message/MessageHandler.h"
#include "gamit/serialize/serializer.h"

namespace gamit
{
	class CMessageManager
	{
	public:
		static CMessageManager * instance();
		void registHandler(int command, const CMessageHandlerBasePtr & handler);
		void __onMessage(CSerializer & __is);

	private:
		CMessageManager();
		~CMessageManager();

		MapMessageHandlerBase _mapMessageHandler;
		static CMessageManager * _inst;
	};
}

#endif