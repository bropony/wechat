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
from gamit.serialize.util import *
from gamit.rmi.rmicore import *
from gamit.serialize.serializer import Serializer
from gamit.serialize.datatype import RmiDataType
import abc
import message.common.publicdef
import message.gate.gatemsg


class DictStrMessage(DictBase):
    def __init__(self):
        super().__init__(str, message.gate.gatemsg.SMessage, 'DictStrMessage')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = str()
            val_ = message.gate.gatemsg.SMessage()
            key_ = _is.readString()
            val_._read(_is)
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeString(item[0])
            item[1]._write(_os)

    def _fromJson(self, js):
        for key_ in js:
            val = message.gate.gatemsg.SMessage()
            val._fromJson(js[key_])
            self[key_] = val

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]._toJson()
        return res

class ITest_Getintlist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, intList):
        _os = self._os
        _os.writeInt(self.msgId)
        intList._write(_os)

        self.sendout()

class ITest_Getdictintstring_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, intStrMap):
        _os = self._os
        _os.writeInt(self.msgId)
        intStrMap._write(_os)

        self.sendout()

class ITest_Getfloatlist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, floatList):
        _os = self._os
        _os.writeInt(self.msgId)
        floatList._write(_os)

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
        intList = message.common.publicdef.SeqInt()
        intList._read(_is)

        self.onResponse(intList)

    @abc.abstractmethod
    def onResponse(self, intList):
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITest_Getdictintstring_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        intStrMap = message.common.publicdef.DictIntString()
        intStrMap._read(_is)

        self.onResponse(intStrMap)

    @abc.abstractmethod
    def onResponse(self, intStrMap):
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITest_Getfloatlist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def _onResponse(self, _is):
        floatList = message.common.publicdef.SeqFloat()
        floatList._read(_is)

        self.onResponse(floatList)

    @abc.abstractmethod
    def onResponse(self, floatList):
        pass

    @abc.abstractmethod
    def onError(self, what, code):
        pass

    @abc.abstractmethod
    def onTimeout(self):
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
    def onError(self, what, code):
        pass

    @abc.abstractmethod
    def onTimeout(self):
        pass


class ITestServant(RmiServant):
    def __init__(self, name):
        super().__init__(name)
        self.methodMap['getIntList'] = self._getIntList
        self.methodMap['getDictIntString'] = self._getDictIntString
        self.methodMap['getFloatList'] = self._getFloatList
        self.methodMap['signup'] = self._signup

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


