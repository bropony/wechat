#
# rmicall
#
# rmiresponse
#

import inspect
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
            if not inspect.isfunction(obj):
                continue
            if func.endswidth("_"):
                continue
            if not func.endswidth("__"):
                continue
            if not func[2:] in self.__class__.__dict__:
                continue
            self.methodMap[func] = obj

    def setRmiServer(self, rmiServer):
        self.rmiServer = rmiServer

    def invoke(self, connId, name, __is):
        if not name in self.methodMap:
            raise SerializeError("{} is not member mthod of {}".format(name, self.name))

        try:
            self.methodMap[name](connId, __is)
        except Exception as ex:
            what = ex.args[0] if len(ex.args) > 0 else "UnkownError"
            code = ex.args[1] if len(ex.args) > 1 else 0
            msgId = ex.args[2] if len(ex.args) > 2 else 0

            __os = Serializer()
            __os.startToWrite()
            __os.writeByte(RmiDataType.RmiException)
            __os.writeInt(msgId)
            __os.writeString(what)
            __os.writeInt(code)

            self.rmiServer.send(connId, __os.getBuffer())


class RmiRequestBase(metaclass=abc.ABCMeta):
    def __init__(self, connId, msgId, servant):
        self.connId = connId
        self.msgId = msgId
        self.servant = servant
        self.__os = Serializer()
        self.__os.startToWrite()
        self.__os.writeByte(RmiDataType.RmiResponse)

    def sendout(self):
        self.servant.rmiServer.send(self.connId, self.__os.getBuffer())

    @abc.abstractmethod
    def __response(self):
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

    def invoke(self, __os, callback):
        self.rmiClient.onCall(__os, callback)

class RmiResponseBase(metaclass=abc.ABCMeta):
    def __init__(self, msgId):
        self.msgId = msgId

    @abc.abstractmethod
    def __onResponse(self, __is):
        pass
