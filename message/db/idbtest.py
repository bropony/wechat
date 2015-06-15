#
# file: idbtest.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *
from gamit.rmi.rmicore import *
from gamit.serialize.serializer import Serializer
from gamit.serialize.datatype import RmiDataType
import abc
import message.common.publicdef
import message.gate.gatemsg
import message.db.main_db


class IDbTest_Sayhello_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, world):
        _os = self._os
        _os.writeInt(self.msgId)
        world._write(_os)

        self.sendout()

class IDbTest_Sayhello_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        world = message.db.main_db.AnRmiTest()
        world._read(_is)

        self.onResponse(world)

    @abc.abstractmethod
    def onResponse(self, world):
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class IDbTestServant(RmiServant):
    def __init__(self, name):
        super().__init__(name)
        self.methodMap['sayhello'] = self._sayhello

    def _sayhello(self, _connId, _msgId, _is):
        hello = message.db.main_db.AnRmiTest()
        hello._read(_is)
        _request = IDbTest_Sayhello_Request(_connId, _msgId, self)
        self.sayhello(hello, _request)

    @abc.abstractmethod
    def sayhello(self, hello, _request):
        pass

class IDbTestProxy(RmiProxy):
    def __init__(self, name):
        super().__init__(name)

    def sayhello(self, _response, hello):
        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('sayhello')
        _msgId = self.getMsgId()
        _os.writeInt(_msgId)
        _response._setMsgId(_msgId)
        hello._write(_os)
        self.invoke(_os, _response)


