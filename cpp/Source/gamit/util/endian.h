#ifndef _CDF_ENDIAN_H_
#define _CDF_ENDIAN_H_

#include "gamit/def/macros.h"

namespace gamit
{
	template <typename T>
		inline T endian( T s )
	{
#ifdef G_LITTLE_ENDIAN
		return s;
#else
		T v1;
		byte_t* p = (byte_t*)&s + sizeof(T) - 1;
		byte_t* q = (byte_t*)&v1;
		switch( sizeof( s ) )
		{
		case 8:
			*q ++ = *p -- ;
			*q ++ = *p -- ;
			*q ++ = *p -- ;
			*q ++ = *p -- ;
		case 4:
			*q ++ = *p -- ;
			*q ++ = *p -- ;
		case 2:
			*q ++ = *p -- ;
		case 1:
			*q = *p;
			break;
		default:
			assert( false );
			break;
		}
		return v1;
#endif
	}
}
#endif
