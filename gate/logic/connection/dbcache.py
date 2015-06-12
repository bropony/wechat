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
from gamit.rmi.proxymanager import ProxyManager
from gamit.app import apptype as AppType
from settings.servant import ServantSetting

from logic.dbback.idbtestcb import IDbTest_Sayhello_callback
from message.db.main_db import AnRmiTest

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
            self.onOpen()
        else:
            self.onClose()

    def __init__(self, channel):
        self.channel = channel

    def onOpen(self):
        Logger.logInfo("ConnectionInfo", "Connected to dbcache")
        ConnectionInfo.setDbCacheOpen(True)

        proxy = ProxyManager.getProxy(AppType.DBCACHE, "IDbTest")
        if proxy:
            for i in range(100):
                msg = AnRmiTest()
                msg.ip = "168.168.168.168"
                msg.shortDesc = "I wanna say hey..."
                msg.passedTimes = i + ServantSetting.getChannelId() * 100
                proxy.sayhello(IDbTest_Sayhello_callback(), msg)

    def onClose(self):
        Logger.logInfo("ConnectionInfo", "dbcache connection closed")
        ConnectionInfo.setDbCacheOpen(False)