#ifndef __GAMIT_UTIL_AUTORUN_H__
#define __GAMIT_UTIL_AUTORUN_H__

#include <functional>

namespace gamit
{
	typedef std::function<void()> AtuoFunc;

	class CAutoRun
	{
	public:
		CAutoRun(AtuoFunc func)
		{
			func();
		}
	};
}

#endif