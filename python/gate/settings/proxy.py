"""
* @name proxy.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/3 19:47
*
* @desc proxy.py
"""

from gamit.singleton.singleton import Singleton
from message.db.idbtest import IDbTestProxy

class ProxySetting(Singleton):
    @staticmethod
    def initDbCacheProxy(client):
        client.addProxy(IDbTestProxy("IDbTest"))
# ###
