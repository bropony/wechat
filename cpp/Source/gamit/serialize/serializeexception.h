#ifndef _GAMIT_SERIALIZE_SERIALIZE_EXCEPTION_H_
#define _GAMIT_SERIALIZE_SERIALIZE_EXCEPTION_H_

#include "gamit/util/exception.h"

namespace gamit
{
	class CSerializeException
		:public CException
	{
	public:
		CSerializeException( const char* buf );
		virtual ~CSerializeException();
	};
}
#endif