"""
* @name application.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/3 10:22
*
* @desc application
"""

import sys
import os

from twisted.internet import reactor

from staticdata.serverconfig import ServerConfigManager
import gamit.app.apptype as AppType
from gamit.app.application import ApplicationBase
from gamit.log.logger import Logger

# settings
from settings.proxy import *
from settings.servant import *
from settings.message import *
from logic.connection.preinvoke import Preinvoke
from logic.connection.dbcache import DbCacheConnectCallback

class Application(ApplicationBase):
    def __init__(self, name="", channelId=0):
        super().__init__(name, channelId)

    # serve as a servant (server side logic)
    def initServant(self):
        if self.channelId:
            channel = ServerConfigManager.getChannelById(self.channelId)
        else:
            channel = ServerConfigManager.getChannelByType(AppType.GATE)

        if not channel:
            Logger.logInfo("Gate Channel not configured:", self.channelId)
            return False

        self.createRmiServer(channel, ServerConfigManager.isDebug)
        self.server.setBeforeInvoke(Preinvoke())

        ServantSetting.initServant(self.server)
        ServantSetting.setChannelId(self.channelId)

        return True

    def initMessageManager(self):
        if not self.messageManager:
            self.messageManager = MessageManager(self.server)

        MessageSetting.initMessangeHandler()
        return True

    def initProxies(self):
        if not self._initDbCacheProxy():
            return False

        if not self._initDbLogProxy():
            return False

        return True

    # serve as a proxy (client side logic)
    def _initDbCacheProxy(self):
        channel = ServerConfigManager.getChannelByType(AppType.DBCACHE)
        if not channel:
            Logger.logInfo("DbCache channel not configured.")
            return False

        dbConnCb = DbCacheConnectCallback(channel)
        rmiClient = self.addProxyByChannel(channel, ServerConfigManager.isDebug, dbConnCb, dbConnCb, [True], [False])

        ProxySetting.initDbCacheProxy(rmiClient)

        return True

    # serve as a proxy (client side logic)
    def _initDbLogProxy(self):
        # todo
        return True


