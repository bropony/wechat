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
from gamit.log.logger import Logger
from gamit.rmi import protocol as Protocol

from gamit.rmi.rmiserver import RmiServer
from gamit.rmi.rmiclient import RmiClient
from gamit.message.messagemanager import MessageManager
from gamit.timer.schedule import Scheduler
from gamit.rmi.sessionmanager import SessionManager

# choose a network protocol
NETWORK_PROTOCOL = Protocol.WEBSOCKET

if NETWORK_PROTOCOL == Protocol.WEBSOCKET:
    from gamit.websocket.ws_acceptor import WsAcceptor as Acceptor
    from gamit.websocket.ws_connector import WsConnector as Connector
elif NETWORK_PROTOCOL == Protocol.ASIO:
    from gamit.websocket.asio_acceptor import AsioAcceptor as Acceptor
    from gamit.websocket.asio_connector import AsioConnector as Connector
else:
    raise Exception("Not network protocol assigned.")

# settings
from settings.proxy import *
from settings.servant import *
from settings.message import *
from logic.connection.preinvoke import Preinvoke
from logic.connection.dbcache import DbCacheConnectCallback

class Application:
    def __init__(self):
        self.server = None
        self.clientMap = {}
        self.messageManager = None
        self.scheduler = Scheduler()

    def start(self):
        self.server.start()
        self.scheduler.start()
        SessionManager.startHeartBeats()

        for _, client in self.clientMap.items():
            client.start()

        reactor.run()

    def stop(self):
        self.server.stop()
        for _, client in self.clientMap.items():
            client.stop()

        #reactor.stop()

    def init(self):
        if not self._initRmiServer():
            return False

        # this must be done before and proxy is initiated...
        if not self._initMessageManager():
            return False

        if not self._initDbCacheProxy():
            return False

        if not self._initDbLogProxy():
            return False

        return True

    # serve as a servant (server side logic)
    def _initRmiServer(self):
        channel = ServerConfigManager.getChannelByType(AppType.GATE)
        if not channel:
            Logger.logInfo("Gate channel not configured.")
            return False

        acceptor = Acceptor(channel.ip, channel.port)
        rmiServer = RmiServer(acceptor, ServerConfigManager.isDebug)
        self.server = rmiServer
        self.server.setBeforeInvoke(Preinvoke())
        self.messageManager = rmiServer.messageManager

        ServantSetting.initServant(self.server)
        return True

    def _initMessageManager(self):
        if not self.messageManager:
            self.messageManager = MessageManager(self.server)

        MessageSetting.initMessangeHandler()
        return True

    # serve as a proxy (client side logic)
    def _initDbCacheProxy(self):
        channel = ServerConfigManager.getChannelByType(AppType.DBCACHE)
        if not channel:
            Logger.logInfo("DbCache channel not configured.")
            return False

        connector = Connector(channel.ip, channel.port)
        rmiClient = RmiClient(channel.type, connector, ServerConfigManager.isDebug)
        dbConnCb = DbCacheConnectCallback(channel)
        rmiClient.setOnOpenCallback(dbConnCb, True)
        rmiClient.setOnCloseCallback(dbConnCb, False)

        self.clientMap[AppType.DBCACHE] = rmiClient
        ProxySetting.initDbCacheProxy(rmiClient)

        return True

    # serve as a proxy (client side logic)
    def _initDbLogProxy(self):
        # todo
        return True


