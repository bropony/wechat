#
# file: itest.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.rmi.rmicore import *
from gamit.serialize.serializer import Serializer
from gamit.serialize.datatype import RmiDataType
import abc
import message.common.publicdef
import message.gate.gatemsg


class ITest_Getintlist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, intList):
        _os = self._os
        _os.writeInt(self.msgId)
        message.common.publicdef.writeSeqInt(_os, intList)

        self.sendout()

class ITest_Getdictintstring_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, intStrMap):
        _os = self._os
        _os.writeInt(self.msgId)
        message.common.publicdef.writeDictIntString(_os, intStrMap)

        self.sendout()

class ITest_Getfloatlist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, floatList):
        _os = self._os
        _os.writeInt(self.msgId)
        message.common.publicdef.writeSeqFloat(_os, floatList)

        self.sendout()

class ITest_Signup_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, loginReturn):
        _os = self._os
        _os.writeInt(self.msgId)
        loginReturn._write(_os)

        self.sendout()

class ITest_Getintlist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        intList = []
        message.common.publicdef.readSeqInt(_is, intList)

        self.onResponse(intList)

    @abc.abstractmethod
    def onResponse(self, intList):
        pass

    @abc.abstractmethod
    def onError(what, code):
        pass


class ITest_Getdictintstring_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        intStrMap = {}
        message.common.publicdef.readDictIntString(_is, intStrMap)

        self.onResponse(intStrMap)

    @abc.abstractmethod
    def onResponse(self, intStrMap):
        pass

    @abc.abstractmethod
    def onError(what, code):
        pass


class ITest_Getfloatlist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        floatList = []
        message.common.publicdef.readSeqFloat(_is, floatList)

        self.onResponse(floatList)

    @abc.abstractmethod
    def onResponse(self, floatList):
        pass

    @abc.abstractmethod
    def onError(what, code):
        pass


class ITest_Signup_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        loginReturn = message.gate.gatemsg.SLoginReturn()
        loginReturn._read(_is)

        self.onResponse(loginReturn)

    @abc.abstractmethod
    def onResponse(self, loginReturn):
        pass

    @abc.abstractmethod
    def onError(what, code):
        pass


class ITestServant(RmiServant):
    def __init__(self, name):
        super().__init__(name)

    def _getIntList(self, _connId, _msgId, _is):
        size = int()
        size = _is.readInt()
        _request = ITest_Getintlist_Request(_connId, _msgId, self)
        self.getIntList(size, _request)

    @abc.abstractmethod
    def getIntList(self, size, _request):
        pass

    def _getDictIntString(self, _connId, _msgId, _is):
        size = int()
        size = _is.readInt()
        _request = ITest_Getdictintstring_Request(_connId, _msgId, self)
        self.getDictIntString(size, _request)

    @abc.abstractmethod
    def getDictIntString(self, size, _request):
        pass

    def _getFloatList(self, _connId, _msgId, _is):
        size = int()
        size = _is.readInt()
        _request = ITest_Getfloatlist_Request(_connId, _msgId, self)
        self.getFloatList(size, _request)

    @abc.abstractmethod
    def getFloatList(self, size, _request):
        pass

    def _signup(self, _connId, _msgId, _is):
        signup = message.gate.gatemsg.SSignup()
        signup._read(_is)
        _request = ITest_Signup_Request(_connId, _msgId, self)
        self.signup(signup, _request)

    @abc.abstractmethod
    def signup(self, signup, _request):
        pass

class ITestProxy(RmiProxy):
    def __init__(self, name):
        super().__init__(name)

    def getIntList(self, _response, size):
        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getIntList')
        _msgId = self.getMsgId()
        _os.writeInt(_msgId)
        _response._setMsgId(_msgId)
        _os.writeInt(size)
        self.invoke(_os, _response)

    def getDictIntString(self, _response, size):
        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getDictIntString')
        _msgId = self.getMsgId()
        _os.writeInt(_msgId)
        _response._setMsgId(_msgId)
        _os.writeInt(size)
        self.invoke(_os, _response)

    def getFloatList(self, _response, size):
        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('getFloatList')
        _msgId = self.getMsgId()
        _os.writeInt(_msgId)
        _response._setMsgId(_msgId)
        _os.writeInt(size)
        self.invoke(_os, _response)

    def signup(self, _response, signup):
        _os = Serializer()
        _os.startToWrite()
        _os.writeByte(RmiDataType.RmiCall)
        _os.writeString(self.name)
        _os.writeString('signup')
        _msgId = self.getMsgId()
        _os.writeInt(_msgId)
        _response._setMsgId(_msgId)
        signup._write(_os)
        self.invoke(_os, _response)


