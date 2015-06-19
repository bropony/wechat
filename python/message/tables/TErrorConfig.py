#
# file: TErrorConfig.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
from gamit.serialize.util import *


class TErrorConfig:
    __slots__ = dict()
    __slots__['errorCode'] = int
    __slots__['errorName'] = str
    __slots__['errorStr'] = str

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of TErrorConfig.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    def __init__(self):
        self.errorCode = int()
        self.errorName = str()
        self.errorStr = str()

    def _read(self, _is):
        self.errorCode = _is.readInt()
        self.errorName = _is.readString()
        self.errorStr = _is.readString()

    def _write(self, _os):
        _os.writeInt(self.errorCode)
        _os.writeString(self.errorName)
        _os.writeString(self.errorStr)

    def _fromJson(self, js):
        if 'errorCode' in js and isinstance(js['errorCode'], int):
            self.errorCode = js['errorCode']
        if 'errorName' in js and isinstance(js['errorName'], str):
            self.errorName = js['errorName']
        if 'errorStr' in js and isinstance(js['errorStr'], str):
            self.errorStr = js['errorStr']

    def _toJson(self):
        js = dict()
        js['errorCode'] = self.errorCode
        js['errorName'] = self.errorName
        js['errorStr'] = self.errorStr
        return js

MessageBlock.register(TErrorConfig)

class SeqTErrorConfig(ListBase):
    def __init__(self):
        super().__init__(TErrorConfig, 'SeqTErrorConfig')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = TErrorConfig()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = TErrorConfig()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

