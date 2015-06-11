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


class TErrorConfig:
    def __init__(self):
        self.errorName = str()
        self.errorCode = int()
        self.errorStr = str()

    def _read(self, _is):
        self.errorName = _is.readString()
        self.errorCode = _is.readInt()
        self.errorStr = _is.readString()

    def _write(self, _os):
        _os.writeString(self.errorName)
        _os.writeInt(self.errorCode)
        _os.writeString(self.errorStr)

    def _fromJson(self, js):
        if 'errorName' in js and isinstance(js['errorName'], str):
            self.errorName = js['errorName']
        if 'errorCode' in js and isinstance(js['errorCode'], int):
            self.errorCode = js['errorCode']
        if 'errorStr' in js and isinstance(js['errorStr'], str):
            self.errorStr = js['errorStr']

    def _toJson(self):
        js = dict()
        js['errorName'] = self.errorName
        js['errorCode'] = self.errorCode
        js['errorStr'] = self.errorStr
        return js

MessageBlock.register(TErrorConfig)

SeqTErrorConfig = list

def readSeqTErrorConfig(_is, valList):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        val = TErrorConfig()
        val._read(_is)
        valList.append(val)

def writeSeqTErrorConfig(_os, valList):
    dataSize = len(valList)
    _os.writeInt(dataSize)
    for val in valList:
        val._write(_os)

def SeqTErrorConfigFromJson(js):
    res = []
    for js_c in js:
        val = TErrorConfig()
        val._fromJson(js_c)
        res.append(val)
    return res

def SeqTErrorConfigToJson(valList):
    res = []
    for val in valList:
        res.append(val._toJson())
    return res

