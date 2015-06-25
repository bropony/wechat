#include "message.h"
#include "message/gate/gatemsg.h"
#include <cstdio>
#include <cstdlib>
#include <gamit/serialize/encrypt.h>

using namespace Test;

void CMessageTest::runTest()
{
	std::string src = "abcdefg";
	std::string dest = src;
	gamit::CEncrypto::simpleEncrypt(dest);

	std::string back = dest;
	gamit::CEncrypto::simpleDecrypt(back);

	std::cout << "src: " << src << std::endl;
	for (auto c : dest)
	{
		std::cout << (unsigned)c << std::endl;
	}

	std::cout << "back: " << back << std::endl;
}

void CMessageTest::resigt()
{
	gamit::CMessageManager::instance()->registHandler(1, new CMsgHandler());
}

void CMessageTest::send()
{
	message::gate::gatemsg::SMessagePtr msg = new message::gate::gatemsg::SMessage();

	for (int i = 0; i < 10; i++)
	{
		msg->intList.push_back(i);

		char buff[100];
		sprintf_s(buff, "%d", i);

		msg->dictStrInt[buff] = i;
	}

	gamit::MessageBlockPtr msgBlock = new gamit::MessageBlock(1, msg);

	gamit::CSerializer __is(msgBlock->getBuffer());
	__is.startToRead();
	byte_t rmiType;
	__is.read(rmiType);

	gamit::CMessageManager::instance()->__onMessage(__is);
}

void CMsgHandler::onMessage(const gamit::MessageBlockPtr & msgBlock)
{
	int command = msgBlock->_command;
}
