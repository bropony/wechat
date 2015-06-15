"""
* @name application
*
* @author ahda86@gmail.com
*
* @date 2015/6/13 9:53
*
* @desc application
"""

import abc
from twisted.internet import reactor
from gamit.timer.schedule import Scheduler
from gamit.rmi.sessionmanager import SessionManager
from gamit.rmi import protocol as Protocol
from gamit.rmi.rmiclient import RmiClient
from gamit.rmi.rmiserver import RmiServer

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

class ApplicationBase(metaclass=abc.ABCMeta):
    def __init__(self, name=None, channelId=0):
        self.name = name
        self.channelId= channelId

        self.stopped = False

        self.rmiServer = None
        self.proxyMap = dict()
        self.messageManager = None

    def start(self):
        # start as Servant
        if self.rmiServer:
            self.rmiServer.start()

        # start Scheduler
        Scheduler.start()

        # start as Proxy
        for _, client in self.proxyMap.items():
            client.start()

        # proxy heart beats
        SessionManager.startHeartBeats()

        # start reactor
        reactor.run()

    def stop(self):
        self.rmiServer.stop()

        for _, client in self.proxyMap.items():
            client.stop()

        self.stopped = True

    def init(self):
        if not self.prepare():
            return False

        if not self.initServant():
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
    def initServant(self):
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

    def createRmiServer(self, channel, isDebug):
        acceptor = Acceptor(channel.ip, channel.port)
        rmiServer = RmiServer(acceptor, isDebug)
        self.server = rmiServer
        self.messageManager = rmiServer.messageManager
        self.channelId = channel.id

        return rmiServer

    def addProxyByChannel(self, channel, isDebug,
                          connOpenCallback=None, connCloseCallback=None, openArgv=[], closeArgv=[]):
        connector = Connector(channel.ip, channel.port)
        rmiClient = RmiClient(channel.type, connector, isDebug)
        rmiClient.setOnOpenCallback(connOpenCallback, *openArgv)
        rmiClient.setOnCloseCallback(connCloseCallback, *closeArgv)

        self.clientMap[channel.type] = rmiClient
        SessionManager.addSession(channel.type, rmiClient)

        return rmiClient
