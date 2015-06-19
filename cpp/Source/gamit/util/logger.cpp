#include "logger.h"
#include <iostream>

void gamit::CLogger::log(const std::string & msg, int level/* = 0*/)
{
	CDateTime now;
	std::cout << "[" << now.asString() << "] " << msg << std::endl;
}
