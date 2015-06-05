#
# @date 2015-05-20
#
# @author ahda86@gmail.com
#
# @desc rmi server
#

from gamit.log.logger import Logger
from gamit.message.messagemanager import MessageManager
from gamit.serialize.serializer import Serializer, SerializeError
from gamit.serialize.datatype import RmiDataType
from twisted.internet import reactor

class RmiServer:
    def __init__(self, acceptor, isDebug, loopInterval=0.03):
        self.acceptor = acceptor
        self.acceptor.setRmiServer(self)
        self.interval = loopInterval
        self.isDebug = isDebug

        self.servantMap = {}
        self.connIdSet = set()
        self.messageManager = MessageManager(self)

    def addServant(self, servant):
        self.servantMap[servant.name] = servant
        servant.setRmiServer(self)

    def start(self):
        self.acceptor.start(self.isDebug)

    def stop(self):
        self.acceptor.stop()

    def onOpen(self, connId):
        self.connIdSet.add(connId)

    def onClose(self, connId):
        if connId in self.connIdSet:
            self.connIdSet.remove(connId)

    def onMessage(self, connId, payload, isBinary):
        try:
            _is = Serializer(payload)
            _is.startToRead()
            rmiType = _is.readByte()
            if rmiType == RmiDataType.RmiCall:
                self.onInvoke(connId, _is)
            elif rmiType == RmiDataType.MessageBlock:
                self.messageManager.onMessage(_is)
            else:
                raise SerializeError("Unknown RmiDataType")
        except Exception as ex:
            Logger.logInfo(ex.__traceback__)

    def close(self, connId, code, reason):
        self.acceptor.close(connId, code, reason)
        if connId in self.connIdSet:
            self.connIdSet.remove(connId)

    def send(self, connId, payload, isBinary=True):
        self.acceptor.send(connId, payload, isBinary)

    def broadcast(self, payload, isBinary=True):
        for connId in self.connIdSet:
            self.send(connId, payload, isBinary)

    def response(self, connId, _os):
        self.send(connId, _os.getBuffer())

    def onInvoke(self, connId, _is):
        try:
            interface = _is.readString()
            method = _is.readString()
            if interface in self.servantMap:
                self.servantMap[interface].invoke(connId, method, _is)
            else:
                raise SerializeError("Servant {} not registered".format(interface))
        except Exception as ex:
            Logger.logInfo(ex.__traceback__)
#end of RmiServer