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

from staticdata.serverconfig import ServerConfigManager
import gamit.app.apptype as AppType
from gamit.log.logger import Logger

class Application:
    def __init__(self):
        self.server = None
        self.clientMap = {}
        self.messageManager = None

    def start(self):
        self.server.start()

        for _, client in self.clientMap:
            client.start()

    def stop(self):
        self.server.stop()
        for _, client in self.clientMap:
            client.stop()

    def init(self):
        if not self._initRmiServer():
            return False

        if not self._initMessageManager():
            return False

        if not self._initRmiClients():
            return False

        return True

    def _initRmiServer(self):
        channel = ServerConfigManager.getChannelByType(AppType.GATE)
        if not channel:
            Logger.logInfo("Gate channel not configured.")

    def _initRmiClients(self):
        pass

    def _initMessageManager(self):
        pass

