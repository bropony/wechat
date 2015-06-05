"""
* @name proxymanager.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/5 19:37
*
* @desc proxymanager.py
"""
from gamit.singleton.singleton import Singleton

class ProxyManager(Singleton):
    _proxyMap = {}

    @classmethod
    def addProxy(cls, channelType, proxy):
        if not channelType in cls._proxyMap:
            cls._proxyMap[channelType] = {}
        cls._proxyMap[channelType][proxy.name] = proxy

    @classmethod
    def getProxy(cls, channelType, name):
        if not channelType in cls._proxyMap:
            return None

        if not name in cls._proxyMap[channelType]:
            return None

        return cls._proxyMap[channelType][name]