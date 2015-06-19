#include "gamit/util/exception.h"
#include <string.h>

using namespace gamit;

CnullptrHandleException::CnullptrHandleException(const char* file , int line )
:CException()
{
	std::ostringstream str;
	str << "CnullptrHandleException " << file << "(" << line << ")";
	_str = str.str();
}
CnullptrHandleException::~CnullptrHandleException()
{
}

