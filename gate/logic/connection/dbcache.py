"""
* @name dbcache.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/9 19:49
*
* @desc dbcache.py

"""

from gamit.log.logger import Logger

class ConnectionInfo:
    _isDbCacheOpen = False
    _isDbLogOpen = False

    @classmethod
    def setDbCacheOpen(cls, isOpen):
        cls._isDbCacheOpen = isOpen

    @classmethod
    def isDbCacheOpen(cls):
        return cls._isDbCacheOpen

    @classmethod
    def setDbLogOpen(cls, isOpen):
        cls._isDbLogOpen = isOpen

    @classmethod
    def isDbLogOpen(cls):
        return cls._isDbLogOpen

class DbCacheConnectCallback:
    def __call__(self, isOpenCallback):
        if isOpenCallback:
            self.onCallback()
        else:
            self.onClose()

    def __init__(self, channel):
        self.channel = channel

    def onOpen(self):
        Logger.logInfo("ConnectionInfo", "Connected to dbcache")
        ConnectionInfo.setDbCacheOpen(True)

    def onClose(self):
        Logger.logInfo("ConnectionInfo", "dbcache connection closed")
        ConnectionInfo.setDbCacheOpen(False)