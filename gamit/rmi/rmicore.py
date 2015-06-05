#
# rmicall
#
# rmiresponse
#

import inspect
from gamit.log.logger import Logger
from gamit.serialize.serializer import SerializeError, Serializer
from gamit.serialize.datatype import RmiDataType
import abc

class RmiMethod:
    pass

class RmiServant:
    def __init__(self, name):
        self.name = name
        self.methodMap = {}
        self.rmiServer = None
        for func in self.__class__.__dict__:
            obj = self.__class__.__dict__[func]
            if not inspect.ismethod(obj):
                continue
            if func.endswith("_"):
                continue
            if not func.startswith("_"):
                continue

            func = func[1:]
            if func not in self.__class__.__dict__:
                continue
            Logger.logDebug("Adding {}.{}".format(name, func))
            self.methodMap[func] = obj

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

    def _setMsgId(self, msgId):
        self._msgId = msgId

    #@abc.abstractmethod
    def _onResponse(self, _is):
        pass

