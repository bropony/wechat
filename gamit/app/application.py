"""
* @name application
*
* @author ahda86@gmail.com
*
* @date 2015/6/13 9:53
*
* @desc application
"""

from threading import Thread
import abc

class ApplicationBase(Thread, metaclass=abc.ABCMeta):
    def __init__(self, name=None, channelId=0, loopInterval=0.03):
        super().__init__(name=name)
        self.channelId= channelId
        self.loopInterval = loopInterval if loopInterval > 0 else 0.03

        self.stopped = False

        self.rmiServer = None
        self.proxyMap = dict()
        self.messageManager = None

    def run(self):
        pass

    def init(self):
        if not self.prepare():
            return False

        if not self.initServer():
            return False

        if not self.initMessageManager():
            return False

        if not self.initProxies():
            return False

        if not self.initEverythingElse():
            return False

        return True

    def prepare(self):
        # Override this method to do something must be done
        # before server, messageManager and proxies initiation.
        #
        # If there is nothing to be done, just don't override me.
        return True

    @abc.abstractmethod
    def initServer(self):
        # Override this method to initiate rmiServer.
        # This method make this application a Rmi Servant (server side role).
        return True

    @abc.abstractmethod
    def initMessageManager(self):
        # Override this method to initiate MessageManager
        return True

    @abc.abstractmethod
    def initProxies(self):
        # Override this method to initiate Rmi proxies
        # This method make this application as client to other Rmi servers.
        return True

    def initEverythingElse(self):
        # Override this method to do something necessary after initServer, initMessageManager
        # and initProxies. This is a protocol paired with method prepare.
        #
        # If there is nothing to be done, just don't override me.
        return True