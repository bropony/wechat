#
# rmicall
#
# rmiresponse
#

import inspect
import abc
import datetime.datetime

from gamit.log.logger import Logger
from gamit.serialize.serializer import SerializeError, Serializer
from gamit.serialize.datatype import RmiDataType

class RmiMethod:
    pass

class RmiServant:
    def __init__(self, name):
        self.name = name
        self.methodMap = {}
        self.rmiServer = None

    def setRmiServer(self, rmiServer):
        self.rmiServer = rmiServer

    def invoke(self, connId, name, _is):
        if not name in self.methodMap:
            raise SerializeError("{} is not member mthod of {}".format(name, self.name))

        msgId = 0
        try:
            msgId = _is.readInt()
            self.methodMap[name](connId, msgId, _is)
        except Exception as ex:
            what = ex.args[0] if len(ex.args) > 0 else "UnkownError"
            code = ex.args[1] if len(ex.args) > 1 else 0

            if not isinstance(what, str):
                what = str(what)

            if not isinstance(code, int):
                code = 0

            _os = Serializer()
            _os.startToWrite()
            _os.writeByte(RmiDataType.RmiException)
            _os.writeInt(msgId)
            _os.writeString(what)
            _os.writeInt(code)

            self.rmiServer.send(connId, _os.getBuffer())


class RmiRequestBase(metaclass=abc.ABCMeta):
    def __init__(self, connId, msgId, servant):
        self.connId = connId
        self.msgId = msgId
        self.servant = servant
        self._os = Serializer()
        self._os.startToWrite()
        self._os.writeByte(RmiDataType.RmiResponse)

    def sendout(self):
        self.servant.rmiServer.send(self.connId, self._os.getBuffer())

    #@abc.abstractmethod
    def response(self):
        pass


class RmiProxy:
    msgId = 0

    @classmethod
    def getMsgId(cls):
        cls.msgId += 1
        return cls.msgId

    def __init__(self, name):
        self.name = name
        self.rmiClient = None

    def setRmiClient(self, rmiClient):
        self.rmiClient = rmiClient

    def invoke(self, _os, callback):
        self.rmiClient.onCall(_os, callback)

class RmiResponseBase(metaclass=abc.ABCMeta):
    def __init__(self):
        self._msgId = 0
        self._createDt = datetime.datetime.now()

    def isExpired(self, now, timeout):
        passed = now - self._createDt
        if passed.total_seconds() >= timeout:
            return True
        return False

    def _setMsgId(self, msgId):
        self._msgId = msgId

    #@abc.abstractmethod
    def _onResponse(self, _is):
        pass

