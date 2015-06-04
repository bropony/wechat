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
from twisted.internet import reactor

class RmiClient:
    def __init__(self, connector, msgMgr, isDebug):
        self.isDebug = isDebug
        self.connector = connector
        self.connector.setRmiClient(self)
        self.messageManager = msgMgr
        self.callbackMap = {}
        self.proxyMap = {}

    def start(self):
        self.connector.start(self.isDebug)

    def stop(self):
        self.connector.stop()
        self.callbackMap = {}

    def addProxy(self, name, proxy):
        self.proxyMap[name] = proxy
        proxy.setRmiClient(self)

    def getProxy(self, name):
        if name in self.proxyMap:
            return self.proxyMap[name]
        else:
            return None

    def onOpen(self, ws):
        pass

    def onClose(self):
        pass

    def onMessage(self, payload, isBinary):
        try:
            __is = Serializer(payload)
            __is.startToRead()
            rmiType = __is.readByte()
            if rmiType == RmiDataType.RmiResponse:
                self.onResponse(__is)
            elif rmiType == RmiDataType.MessageBlock:
                self.messageManager.onMessage(__is)
            else:
                raise SerializeError("Unknown RmiDataType")
        except Exception as ex:
            Logger.logInfo(ex.__traceback__)

    def sendMessage(self, command, toIdList, data):
        msg = MessageBlock(command, toIdList, data)
        self.connector.send(msg.getOsBuffer(), True)

    def onResponse(self, __is):
        msgId = __is.readInt()
        if msgId in self.callbackMap:
            self.callbackMap[msgId].__onResponse(__is)

    def onCall(self, __os, callback):
        self.connector.send(__os.getBuffer(), True)
        self.callbackMap[callback.__msgId] = callback