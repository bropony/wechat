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
        __os = self.__os
        __os.writeInt(self.msgId)
        message.common.publicdef.writeSeqInt(__os, intList)

        self.sendout()

class ITest_Getdictintstring_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, intStrMap):
        __os = self.__os
        __os.writeInt(self.msgId)
        message.common.publicdef.writeDictIntString(__os, intStrMap)

        self.sendout()

class ITest_Getfloatlist_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, floatList):
        __os = self.__os
        __os.writeInt(self.msgId)
        message.common.publicdef.writeSeqFloat(__os, floatList)

        self.sendout()

class ITest_Signup_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, loginReturn):
        __os = self.__os
        __os.writeInt(self.msgId)
        loginReturn.write__(__os)

        self.sendout()

class ITest_Getintlist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def __onResponse(self, __is):
        intList = []
        message.common.publicdef.readSeqInt(__is, intList)

        self.onResponse(intList)

    @abc.abstractmethod
    def onResponse(self, intList):
        pass


class ITest_Getdictintstring_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def __onResponse(self, __is):
        intStrMap = {}
        message.common.publicdef.readDictIntString(__is, intStrMap)

        self.onResponse(intStrMap)

    @abc.abstractmethod
    def onResponse(self, intStrMap):
        pass


class ITest_Getfloatlist_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def __onResponse(self, __is):
        floatList = []
        message.common.publicdef.readSeqFloat(__is, floatList)

        self.onResponse(floatList)

    @abc.abstractmethod
    def onResponse(self, floatList):
        pass


class ITest_Signup_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def __onResponse(self, __is):
        loginReturn = message.gate.gatemsg.SLoginReturn()
        loginReturn.read__(__is)

        self.onResponse(loginReturn)

    @abc.abstractmethod
    def onResponse(self, loginReturn):
        pass


class ITestServant(RmiServant):
    def __init__(self, name):
        super().__init__(name)

    def __getIntList(self, __connId, __msgId, __is):
        size = int()
        size = __is.readInt()
        __request = ITest_Getintlist_Request(__connId, __msgId, self)
        self.getIntList(size, __request)

    @abc.abstractmethod
    def getIntList(self, size, __request):
        pass

    def __getDictIntString(self, __connId, __msgId, __is):
        size = int()
        size = __is.readInt()
        __request = ITest_Getdictintstring_Request(__connId, __msgId, self)
        self.getDictIntString(size, __request)

    @abc.abstractmethod
    def getDictIntString(self, size, __request):
        pass

    def __getFloatList(self, __connId, __msgId, __is):
        size = int()
        size = __is.readInt()
        __request = ITest_Getfloatlist_Request(__connId, __msgId, self)
        self.getFloatList(size, __request)

    @abc.abstractmethod
    def getFloatList(self, size, __request):
        pass

    def __signup(self, __connId, __msgId, __is):
        signup = message.gate.gatemsg.SSignup()
        signup.read__(__is)
        __request = ITest_Signup_Request(__connId, __msgId, self)
        self.signup(signup, __request)

    @abc.abstractmethod
    def signup(self, signup, __request):
        pass

class ITestProxy(RmiProxy):
    def __init__(self, name):
        super().__init__(name)

    def getIntList(self, __response, size):
        __os = Serializer()
        __os.startToWrite()
        __os.writeByte(RmiDataType.RmiCall)
        __msgId = self.getMsgId()
        __os.writeInt(__msgId)
        __response.__setMsgId(__msgId)
        __os.writeInt(size)
        self.invoke(__os, __response)

    def getDictIntString(self, __response, size):
        __os = Serializer()
        __os.startToWrite()
        __os.writeByte(RmiDataType.RmiCall)
        __msgId = self.getMsgId()
        __os.writeInt(__msgId)
        __response.__setMsgId(__msgId)
        __os.writeInt(size)
        self.invoke(__os, __response)

    def getFloatList(self, __response, size):
        __os = Serializer()
        __os.startToWrite()
        __os.writeByte(RmiDataType.RmiCall)
        __msgId = self.getMsgId()
        __os.writeInt(__msgId)
        __response.__setMsgId(__msgId)
        __os.writeInt(size)
        self.invoke(__os, __response)

    def signup(self, __response, signup):
        __os = Serializer()
        __os.startToWrite()
        __os.writeByte(RmiDataType.RmiCall)
        __msgId = self.getMsgId()
        __os.writeInt(__msgId)
        __response.__setMsgId(__msgId)
        signup.write__(__os)
        self.invoke(__os, __response)


