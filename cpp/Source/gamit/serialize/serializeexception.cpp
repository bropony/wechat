#include "gamit/serialize/serializeexception.h"

using namespace gamit;

CSerializeException::
CSerializeException( const char* exp )
	:CException( exp , ExceptionCodeSerialize )
{
}

CSerializeException::~CSerializeException()
{

}
