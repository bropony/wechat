"""
* @name rmiclient.py
*
* @author ahda86@gmail.com
*
* @date 2015/5/23 12:02
*
* @desc rmiclient.py
"""

from gamit.log.logger import Logger
from gamit.message.messagemanager import MessageManager
from gamit.message.message import MessageBlock
from gamit.serialize.serializer import Serializer, SerializeError
from gamit.serialize.datatype import RmiDataType
from gamit.rmi.proxymanager import ProxyManager
from gamit.rmi.sessionmanager import SessionManager
from twisted.internet import reactor

class RmiClient:
    def __init__(self, channelType, connector, isDebug):
        self.channelType = channelType
        self.isDebug = isDebug
        self.connector = connector
        self.connector.setRmiClient(self)
        self.messageManager = MessageManager
        self.callbackMap = {}
        self.proxyMap = {}
        self.onOpenCallback = None
        self.openCallArgv = []

        SessionManager.addSession(channelType, self)

    def start(self):
        self.connector.start(self.isDebug)

    def stop(self):
        self.connector.stop()
        self.callbackMap = {}

    def setOnOpenCallback(self, cb, *argv):
        self.onOpenCallback = cb
        self.openCallArgv = argv

    def addProxy(self, proxy):
        self.proxyMap[proxy.name] = proxy
        proxy.setRmiClient(self)
        ProxyManager.addProxy(self.channelType, proxy)

    def getProxy(self, name):
        if name in self.proxyMap:
            return self.proxyMap[name]
        else:
            return None

    def onOpen(self, ws):
        if self.onOpenCallback:
            cb = self.onOpenCallback
            cb(*self.openCallArgv)

    def onClose(self):
        pass

    def onMessage(self, payload, isBinary):
        try:
            _is = Serializer(payload)
            _is.startToRead()
            rmiType = _is.readByte()
            if rmiType == RmiDataType.RmiResponse:
                self.onResponse(_is)
            elif rmiType == RmiDataType.RmiException:
                self.onError(_is)
            elif rmiType == RmiDataType.MessageBlock:
                self.messageManager.onMessage(_is)
            else:
                raise SerializeError("Unknown RmiDataType")
        except Exception as ex:
            Logger.logInfo(ex)

    def sendMessage(self, command, toIdList, data):
        msg = MessageBlock(command, toIdList, data)
        self.connector.send(msg.getOsBuffer(), True)

    def onResponse(self, _is):
        msgId = _is.readInt()
        if msgId in self.callbackMap:
            self.callbackMap[msgId]._onResponse(_is)

    def onError(self, _is):
        msgId = _is.readInt()
        what = _is.readString()
        code = _is.readInt()
        if msgId in self.callbackMap:
            self.callbackMap[msgId].onError(what, code)

    def onCall(self, _os, callback):
        self.connector.send(_os.getBuffer(), True)
        self.callbackMap[callback._msgId] = callback

    def heartbeat(self):
        self.connector.ws.sendPing()