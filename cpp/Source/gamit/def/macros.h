#ifndef __GAMIT_DEF_MACROS_H__
#define __GAMIT_DEF_MACROS_H__

#ifdef _WIN32
#define G_WIN32
#endif

#if defined(G_WIN32) || defined(__i386) || defined(__x86_64)
#define G_LITTLE_ENDIAN   1
#endif

// network type
#define G_USE_WEBSOCKET 1
//#define G_USE_ASIO 1

#endif //__GAMIT_DEF_MACROS_H__