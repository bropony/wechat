#ifndef __GAMIT_DEF_TYPES_H__
#define __GAMIT_DEF_TYPES_H__

#include "gamit/def/macros.h"

#ifndef byte_t
typedef unsigned char byte_t;
#endif

#ifndef long64_t
#ifdef _WIN32
typedef unsigned __int64 ulong64_t;
typedef __int64 long64_t;
#else
typedef long long  long64_t;
typedef unsigned long long ulong64_t;
#endif
#endif

#endif