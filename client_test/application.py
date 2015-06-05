"""
* @name application.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:18
*
* @desc application.py
"""

from twisted.internet import reactor
from staticdata.serverconfig import ServerConfigManager

from gamit.timer.schedule import Scheduler
from gamit.rmi.rmiclient import RmiClient
from gamit.message.messagemanager import MessageManager
from gamit.websocket.ws_connector import WsConnector as Connector
import gamit.app.apptype as AppType
from gamit.log.logger import Logger

from settings.proxy import ProxySetting
from test.runtest import runTest
from core.enginehelper import EngineHelper

class Application:
    def __init__(self):
        self.client = None
        self.messageManager = None
        self.scheduler = Scheduler()

    def start(self):
        self.client.start()
        self.scheduler.start()
        reactor.run()

    def stop(self):
        self.client.stop()

    def init(self):
        if not self.initMessageManager():
            return False

        if not self.initClient():
            return False

        return True

    def initMessageManager(self):
        self.messageManager = MessageManager(None)
        EngineHelper.setMessageManager(self.messageManager)
        return True

    def initClient(self):
        channel = ServerConfigManager.getChannelByType(AppType.GATE)
        if not channel:
            Logger.logInfo("Gate channel not configured.")
            return False

        Logger.logInfo("Init Proxy {}:{}".format(channel.ip, channel.port))
        connector = Connector(channel.ip, channel.port)
        self.client = RmiClient(connector, self.messageManager, ServerConfigManager.isDebug)

        self.client.setOnOpenCallback(runTest)
        EngineHelper.setClient(self.client)

        ProxySetting.initGateProxy(self.client)
        return True
# end of Application
