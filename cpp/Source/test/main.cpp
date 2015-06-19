#include <cstdio>

#include <datetime/DatetimeTest.h>
#include <ptr_test/shareptr.h>
#include <engine_test/message.h>

int main(int argc, char ** argv)
{
	//Test::CDatetimeTest::dateTimeTest();

	//Test::CPtrTest::runTest();

	Test::CMessageTest::runTest();

	int dummy;
	std::printf("Press Enter to exit...");
	std::getchar();

	return 0;
}