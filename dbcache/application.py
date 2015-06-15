"""
* @name application.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/9 19:26
*
* @desc application.py
"""

from staticdata.serverconfig import ServerConfigManager
import gamit.app.apptype as AppType
from gamit.log.logger import Logger
from gamit.app.application import ApplicationBase
from gamit.message.messagemanager import MessageManager
from gamit.timer.schedule import Scheduler
from gamit.rmi.sessionmanager import SessionManager
from gamit.mongodb.database import MongoDatabase


# settings
from settings.servant import *
from settings.message import *

class Application(ApplicationBase):
    def __init__(self, name=None, channelId=0):
        super().__init__(name, channelId)

    # serve as a servant (server side logic)
    def initServant(self):
        channel = ServerConfigManager.getChannelByType(AppType.DBCACHE)
        if not channel:
            Logger.logInfo("DBCACHE channel not configured.")
            return False

        rmiServer = self.createRmiServer(channel, ServerConfigManager.isDebug)
        ServantSetting.initServant(rmiServer)
        return True

    def initMessageManager(self):
        if not self.messageManager:
            self.messageManager = MessageManager(self.server)

        MessageSetting.initMessangeHandler()
        return True

    def initProxies(self):
        # nothing to be done
        return True

# end of Application
