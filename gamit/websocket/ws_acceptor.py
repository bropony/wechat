#
# network server acceptor using websocket
#

from twisted.internet import  reactor
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactor
from gamit.log.logger import Logger
import logging

class _WSServerProtocol(WebSocketServerProtocol):
    """
    websocket server protocol
    """
    connIdBase = 0 #connection id generator
    @classmethod
    def getConnId(cls):
        cls.connIdBase += 1
        return cls.connIdBase


    #def __init__(self, proxy):
    #    super().__init__()
    #   self.proxy = proxy

    def onConnect(self, request):
        self.connId = self.getConnId()
        Logger.logInfo("Connection Request from ", request.peer, ". connId: ", self.connId)

        self.proxy.onConnect(self.connId, request.peer)
        
    def onOpen(self):
        Logger.logInfo("Connection opend. ", self.connId)
        self.proxy.onOpen(self.connId, self)

    def onMessage(self, payload, isBinary):
        self.proxy.onMessage(self.connId, payload, isBinary)

    def onClose(self, wasClean, code, reason):
        Logger.logInfo("Connection colsed. ", self.connId)
        self.proxy.onClose(self.connId, code, reason)


class WsAcceptor:
    """
    web socket acceptor
    """
    def __init__(self, ip, port):
        self.connMap = {}
        self.factory = None
        self.ip = ip
        self.port = port

        self.running = False

    def setRmiServer(self, rmiServer):
        self.rmiServer = rmiServer
    
    ####
    def start(self, isDebug):
        wsUrl = "ws://{}:{}".format(self.ip, self.port)

        factory = WebSocketServerFactory(wsUrl, debug=isDebug)
        _WSServerProtocol.proxy = self
        factory.protocol = _WSServerProtocol

        reactor.listenTCP(self.port, factory)

        self.factory = factory
        self.running = True
    
    ####
    def stop(self):
        self.running = False

        for connId in self.connMap:
            self.connMap[connId].sendClose()

        self.connMap = {}


    ####
    def onConnect(self, connId, peer):
        pass

    def onOpen(self, connId, ws):
        if connId not in self.connMap:
            self.connMap[connId] = ws
            self.rmiServer.onOpen(connId)
        else:
            Logger.log("[WsAcceptor.onOpen]", "Critical Error: ", connId, logLevel=logging.ERROR)

    def onMessage(self, connId, payload, isBinary):
        if connId not in self.connMap:
            return

        self.rmiServer.onMessage(connId, payload, isBinary)


    def onClose(self, connId, code, reason):
        if connId not in self.connMap:
            return

        self.rmiServer.onClose(connId)
        del self.connMap[connId]


    def close(self, connId, code, reason):
        if connId not in self.connMap:
            return

        conn = self.connMap[connId]
        try:
            conn.sendClose(code, reason)
            del self.connMap[connId]

        except Exception as ex:
            Logger.log("[WsAcceptor.close]", ex.__traceback__)


    def send(self, connId, payload, isBinary):
        if connId not in self.connMap:
            return

        conn = self.connMap[connId]
        try:
            conn.sendMessage(payload, isBinary)
        except Exception as ex:
            Logger.log("[WsAcceptor.send]", ex.__traceback__)

####
####
