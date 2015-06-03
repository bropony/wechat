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

class ProxySetting(Singleton):
    def __init__(self):
        super().__init__()

    @staticmethod
    def initDbCacheProxy(client):
        pass