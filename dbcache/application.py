"""
* @name application.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/9 19:26
*
* @desc application.py
"""

from twisted.internet import reactor

from staticdata.serverconfig import ServerConfigManager
import gamit.app.apptype as AppType
from gamit.log.logger import Logger
from gamit.rmi import protocol as Protocol

from gamit.rmi.rmiserver import RmiServer
from gamit.message.messagemanager import MessageManager
from gamit.timer.schedule import Scheduler
from gamit.rmi.sessionmanager import SessionManager
from gamit.mongodb.database import MongoDatabase

# choose a network protocol
NETWORK_PROTOCOL = Protocol.WEBSOCKET

if NETWORK_PROTOCOL == Protocol.WEBSOCKET:
    from gamit.websocket.ws_acceptor import WsAcceptor as Acceptor
elif NETWORK_PROTOCOL == Protocol.ASIO:
    from gamit.websocket.asio_acceptor import AsioAcceptor as Acceptor
else:
    raise Exception("Not network protocol assigned.")

# settings
from settings.servant import *
from settings.message import *

class Application:
    def __init__(self):
        self.server = None
        self.clientMap = {}
        self.messageManager = None
        self.scheduler = Scheduler()

    def start(self):
        self.server.start()
        self.scheduler.start()
        #SessionManager.startHeartBeats()

        for _, client in self.clientMap.items():
            client.start()

        reactor.run()

    def stop(self):
        self.server.stop()
        for _, client in self.clientMap:
            client.stop()

        MongoDatabase.stop()

    def init(self):
        if not MongoDatabase.start():
            return False

        if not self._initRmiServer():
            return False

        # this must be done before and proxy is initiated...
        if not self._initMessageManager():
            return False

        return True

    # serve as a servant (server side logic)
    def _initRmiServer(self):
        channel = ServerConfigManager.getChannelByType(AppType.DBCACHE)
        if not channel:
            Logger.logInfo("DBCACHE channel not configured.")
            return False

        acceptor = Acceptor(channel.ip, channel.port)
        rmiServer = RmiServer(acceptor, ServerConfigManager.isDebug)
        self.server = rmiServer
        self.messageManager = rmiServer.messageManager

        ServantSetting.initServant(self.server)
        return True

    def _initMessageManager(self):
        if not self.messageManager:
            self.messageManager = MessageManager(self.server)

        MessageSetting.initMessangeHandler()
        return True

# end of Application
