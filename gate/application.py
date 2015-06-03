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
        return True

    def _initRmiServer(self, ip, port):
        pass

    def _initMessageManager(self):
        pass

