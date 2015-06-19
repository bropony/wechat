#include <datetime/DatetimeTest.h>

#include <gamit/util/datetime.h>
#include <iostream>

using namespace Test;
using namespace gamit;

void CDatetimeTest::dateTimeTest()
{
	CDateTime dt;

	CDateTime dt2(2014, 11, 11, 11, 11, 11, 0);

	int totalSecs11 = dt.getTotalSecond();
	int totalSecs21 = dt2.getTotalSecond();
	int totalSecs12 = dt.getTotalSecond();
	int totalSecs22 = dt2.getTotalSecond();

	std::cout << dt.asString() << std::endl;

	std::cout << totalSecs11 << ", " << totalSecs12 << ", "
		<< totalSecs21 << ", " << totalSecs22 << std::endl;
}
