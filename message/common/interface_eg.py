#
# file: interface_eg.py
#
# date: 2015-06-02 16:18:10.634722
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
import message.common.struct_eg


def readSeqAddress(__is, valList):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        val = message.common.struct_eg.SAddress()
        val.__read(__is)
        valList.append(val)

def writeSeqAddress(__os, valList):
    dataSize = len(valList)
    __os.writeInt(dataSize)
    for val in valList:
        val.__write(__os)

def readDictIntSAddress(__is, valDict):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        key_ = int()
        val_ = message.common.struct_eg.SAddress()
        key_ = __is.readInt()
        val_.__read(__is)
        valDict[key_] = val_

def writeDictIntSAddress(__os, valDict):
    dataSize = len(valDict)
    __os.writeInt(dataSize)
    for item in valDict.items():
        __os.writeInt(item[0])
        item[1].__write(__os)

class ITest_Sayhello_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        __os = self.__os
        __os.writeInt(self.msgId)

        self.sendout()

class ITest_Search_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, human):
        __os = self.__os
        __os.writeInt(self.msgId)
        human.__write(__os)

        self.sendout()

class ITest_Alongfunc_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, no, iDonot):
        __os = self.__os
        __os.writeInt(self.msgId)
        __os.writeInt(no)
        __os.writeString(iDonot)

        self.sendout()

class ITest_Somethingwrong_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        __os = self.__os
        __os.writeInt(self.msgId)

        self.sendout()

class ITest_Hey_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self, how):
        __os = self.__os
        __os.writeInt(self.msgId)
        message.common.struct_eg.writeDictIntString(__os, how)

        self.sendout()

class ITest_Sayhello_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def __onResponse(self, __is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        pass


class ITest_Search_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def __onResponse(self, __is):
        human = message.common.struct_eg.SHuman()
        human.__read(__is)

        self.onResponse(human)

    @abc.abstractmethod
    def onResponse(self, human):
        pass


class ITest_Alongfunc_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def __onResponse(self, __is):
        no = int()
        no = __is.readInt()
        iDonot = str()
        iDonot = __is.readString()

        self.onResponse(no, iDonot)

    @abc.abstractmethod
    def onResponse(self, no, iDonot):
        pass


class ITest_Somethingwrong_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def __onResponse(self, __is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        pass


class ITest_Hey_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def __onResponse(self, __is):
        how = {}
        message.common.struct_eg.readDictIntString(__is, how)

        self.onResponse(how)

    @abc.abstractmethod
    def onResponse(self, how):
        pass


class ITestServant(RmiServant):
    def __init__(self, name):
        super.__init__(name)

    def __sayHello(self, __connId, __msgId, __is):
        __request = ITest_Sayhello_Request(__connId, __msgId, self)
        self.sayHello(__request)

    @abc.abstractmethod
    def sayHello(self, __request):
        pass

    def __search(self, __connId, __msgId, __is):
        name = str()
        name = __is.readString()
        __request = ITest_Search_Request(__connId, __msgId, self)
        self.search(name, __request)

    @abc.abstractmethod
    def search(self, name, __request):
        pass

    def __aLongFunc(self, __connId, __msgId, __is):
        yes = int()
        yes = __is.readInt()
        iDo = str()
        iDo = __is.readString()
        __request = ITest_Alongfunc_Request(__connId, __msgId, self)
        self.aLongFunc(yes, iDo, __request)

    @abc.abstractmethod
    def aLongFunc(self, yes, iDo, __request):
        pass

    def __somethingWrong(self, __connId, __msgId, __is):
        __request = ITest_Somethingwrong_Request(__connId, __msgId, self)
        self.somethingWrong(__request)

    @abc.abstractmethod
    def somethingWrong(self, __request):
        pass

    def __hey(self, __connId, __msgId, __is):
        what = []
        message.common.struct_eg.readSeqInt(__is, what)
        __request = ITest_Hey_Request(__connId, __msgId, self)
        self.hey(what, __request)

    @abc.abstractmethod
    def hey(self, what, __request):
        pass

class ITestProxy(RmiProxy):
    def __init__(self,  msgId):
        super().__init__(msgId)

    def sayHello(self, __response):
        __os = Serializer()
        __os.startToWrite()
        __os.writeByte(RmiDataType.RmiCall)
        __msgId = self.getMsgId()
        __os.writeInt(__msgId)
        __response.__setMsgId(__msgId)
        self.invoke(__os, __response)

    def search(self, __response, name):
        __os = Serializer()
        __os.startToWrite()
        __os.writeByte(RmiDataType.RmiCall)
        __msgId = self.getMsgId()
        __os.writeInt(__msgId)
        __response.__setMsgId(__msgId)
        __os.writeString(name)
        self.invoke(__os, __response)

    def aLongFunc(self, __response, yes, iDo):
        __os = Serializer()
        __os.startToWrite()
        __os.writeByte(RmiDataType.RmiCall)
        __msgId = self.getMsgId()
        __os.writeInt(__msgId)
        __response.__setMsgId(__msgId)
        __os.writeInt(yes)
        __os.writeString(iDo)
        self.invoke(__os, __response)

    def somethingWrong(self, __response):
        __os = Serializer()
        __os.startToWrite()
        __os.writeByte(RmiDataType.RmiCall)
        __msgId = self.getMsgId()
        __os.writeInt(__msgId)
        __response.__setMsgId(__msgId)
        self.invoke(__os, __response)

    def hey(self, __response, what):
        __os = Serializer()
        __os.startToWrite()
        __os.writeByte(RmiDataType.RmiCall)
        __msgId = self.getMsgId()
        __os.writeInt(__msgId)
        __response.__setMsgId(__msgId)
        message.common.struct_eg.writeSeqInt(__os, what)
        self.invoke(__os, __response)


class ICheck_Oops_Request(RmiRequestBase):
    def __init__(self, connId, msgId, servant):
        super().__init__(connId, msgId, servant)

    def response(self):
        __os = self.__os
        __os.writeInt(self.msgId)

        self.sendout()

class ICheck_Oops_Response(RmiResponseBase):
    def __init__(self):
        super().__init__()

    def __onResponse(self, __is):

        self.onResponse()

    @abc.abstractmethod
    def onResponse(self):
        pass


class ICheckServant(RmiServant):
    def __init__(self, name):
        super.__init__(name)

    def __oops(self, __connId, __msgId, __is):
        __request = ICheck_Oops_Request(__connId, __msgId, self)
        self.oops(__request)

    @abc.abstractmethod
    def oops(self, __request):
        pass

class ICheckProxy(RmiProxy):
    def __init__(self,  msgId):
        super().__init__(msgId)

    def oops(self, __response):
        __os = Serializer()
        __os.startToWrite()
        __os.writeByte(RmiDataType.RmiCall)
        __msgId = self.getMsgId()
        __os.writeInt(__msgId)
        __response.__setMsgId(__msgId)
        self.invoke(__os, __response)


