"""
* @name ws_connector.py
*
* @author ahda86@gmail.com
*
* @date 2015/5/25 16:02
*
* @desc ws_connector.py
"""
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet import  reactor
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
from gamit.log.logger import Logger
import logging

class _WSClientProtocol(WebSocketClientProtocol):
    def getProxy(self):
        if not self.factory:
            print("Oops")
        return self.factory.__connector

    def onConnect(self, response):
        Logger.logInfo("Connect to ", response.peer)
        self.getProxy().onConnect(self)

    def onOpen(self):
        Logger.logInfo("WS connection opened")
        self.getProxy().onOpen(self)

    def onMessage(self, payload, isBinary):
        self.getProxy().onMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        Logger.logInfo("WS connection closed. ", reason)
        self.getProxy().onClose(code, reason)


class MyClientFactory(WebSocketClientFactory, ReconnectingClientFactory):

    protocol = _WSClientProtocol

    def clientConnectionFailed(self, connector, reason):
        print("Client connection failed .. retrying ..")
        self.retry(connector)

    def clientConnectionLost(self, connector, reason):
        print("Client connection lost .. retrying ..")
        self.retry(connector)

class WsConnector:
    """
    web socket connector
    """
    def __init__(self, ip, port):
        self.ws = None
        self.factory = None
        self.ip = ip
        self.port = port

        self.running = False

    def setRmiClient(self, rmiClient):
        self.rmiClient = rmiClient

    ####
    def start(self, isDebug):
        wsUrl = "ws://{}:{}".format(self.ip, self.port)

        Logger.logInfo("Connecting to {}".format(wsUrl))
        factory = MyClientFactory(wsUrl, debug=isDebug)
        factory.__connector = self
        reactor.connectTCP(self.ip, self.port, factory)

        self.factory = factory
        self.running = True

    ####
    def stop(self):
        self.running = False
        self.close()

    ####
    def onConnect(self, ws):
        #self.rmiClient.onConnect(ws)
        pass

    def onOpen(self, ws):
        self.rmiClient.onOpen(ws)
        self.ws = ws
        self.running = True

    def onMessage(self, payload, isBinary):
        self.rmiClient.onMessage(payload, isBinary)

    def onClose(self, code, reason):
        self.rmiClient.onClose()
        self.ws = None
        self.running = False

    def close(self):
        if self.ws:
            self.ws.sendClose()
            self.ws = None

    def send(self, payload, isBinary=True):
        if not self.running:
            Logger.logInfo("WsConnector.send", " Connect closed")
            return

        try:
            self.ws.sendMessage(payload, isBinary)
        except Exception as ex:
            Logger.log("[WsConnector.send]", ex.__traceback__)
####
