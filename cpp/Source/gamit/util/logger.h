#ifndef __GAMIT_UTIL_LOGGER_H__
#define __GAMIT_UTIL_LOGGER_H__

#include "gamit/def/macros.h"
#include <string>
#include <sstream>
#include "gamit/util/datetime.h"

#define G_LOG_INFO(X) \
    { \
		std::ostringstream __os; \
	    __os << X; \
        CLogger::log(__os.str(), 1); \
	}

#ifndef _DEBUG
# define G_LOG_DEBUG(X) NULL
#else
# define G_LOG_DEBUG(X) \
   { \
        std::istringstream __is; \
	    __is << X; CLogger::log(__is.str(), 0); \
   }
#endif

namespace gamit
{
	class CLogger
	{
	public:
		static void log(const std::string & msg, int level = 0);
	};
}


#endif