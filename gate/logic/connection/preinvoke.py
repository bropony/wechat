"""
* @name preinvoke.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/9 20:12
*
* @desc preinvoke.py
"""

from logic.connection.dbcache import ConnectionInfo

class Preinvoke:
    def __call__(self, *args, **kwargs):
        if not ConnectionInfo.isDbCacheOpen():
            return "Database Not Initiated"

        return None
