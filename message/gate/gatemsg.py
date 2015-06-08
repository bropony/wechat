#
# file: gatemsg.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
import message.common.publicdef


def readSeqSeqInt(_is, valList):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        val = []
        message.common.publicdef.readSeqInt(_is, val)
        valList.append(val)

def writeSeqSeqInt(_os, valList):
    dataSize = len(valList)
    _os.writeInt(dataSize)
    for val in valList:
        message.common.publicdef.writeSeqInt(_os, val)

def SeqSeqIntFromJson(js):
    res = []
    for js_c in js:
        val = message.common.publicdef.SeqIntFromJson(js_c)
        res.append(val)
    return res

def SeqSeqIntToJson(valList):
    res = []
    for val in valList:
        tmp = message.common.publicdef.SeqIntToJson(val)
        res.append(tmp)
    return res

def readSeqDictIntInt(_is, valList):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        val = {}
        message.common.publicdef.readDictIntInt(_is, val)
        valList.append(val)

def writeSeqDictIntInt(_os, valList):
    dataSize = len(valList)
    _os.writeInt(dataSize)
    for val in valList:
        message.common.publicdef.writeDictIntInt(_os, val)

def SeqDictIntIntFromJson(js):
    res = []
    for js_c in js:
        val = message.common.publicdef.DictIntIntFromJson(js_c)
        res.append(val)
    return res

def SeqDictIntIntToJson(valList):
    res = []
    for val in valList:
        tmp = message.common.publicdef.DictIntIntToJson(val)
        res.append(tmp)
    return res

def readDictDictStringInt(_is, valDict):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        key_ = int()
        val_ = {}
        key_ = _is.readInt()
        message.common.publicdef.readDictStringInt(_is, val_)
        valDict[key_] = val_

def writeDictDictStringInt(_os, valDict):
    dataSize = len(valDict)
    _os.writeInt(dataSize)
    for item in valDict.items():
        _os.writeInt(item[0])
        message.common.publicdef.writeDictStringInt(_os, item[1])

def DictDictStringIntFromJson(js):
    res = dict()
    for key_ in js:
        res[key_] = message.common.publicdef.DictStringIntFromJson(js[key_])
    return res

def DictDictStringIntToJson(valDict):
    res = dict()
    for key_ in valDict:
        res[key_] = message.common.publicdef.DictStringIntToJson(valDict[key_])
    return res

class SSignup:
    def __init__(self):
        self.username = str()
        self.nickname = str()
        self.password = str()
        self.sex = int()

    def _read(self, _is):
        self.username = _is.readString()
        self.nickname = _is.readString()
        self.password = _is.readString()
        self.sex = _is.readInt()

    def _write(self, _os):
        _os.writeString(self.username)
        _os.writeString(self.nickname)
        _os.writeString(self.password)
        _os.writeInt(self.sex)

    def _fromJson(self, js):
        if 'username' in js and isinstance(js['username'], str):
            self.username = js['username']
        if 'nickname' in js and isinstance(js['nickname'], str):
            self.nickname = js['nickname']
        if 'password' in js and isinstance(js['password'], str):
            self.password = js['password']
        if 'sex' in js and isinstance(js['sex'], int):
            self.sex = js['sex']

    def _toJson(self):
        js = dict()
        js['username'] = self.username
        js['nickname'] = self.nickname
        js['password'] = self.password
        js['sex'] = self.sex
        return js

MessageBlock.register(SSignup)

class SLogin:
    def __init__(self):
        self.username = str()
        self.password = str()

    def _read(self, _is):
        self.username = _is.readString()
        self.password = _is.readString()

    def _write(self, _os):
        _os.writeString(self.username)
        _os.writeString(self.password)

    def _fromJson(self, js):
        if 'username' in js and isinstance(js['username'], str):
            self.username = js['username']
        if 'password' in js and isinstance(js['password'], str):
            self.password = js['password']

    def _toJson(self):
        js = dict()
        js['username'] = self.username
        js['password'] = self.password
        return js

MessageBlock.register(SLogin)

class SLoginReturn:
    def __init__(self):
        self.userId = int()
        self.username = str()
        self.nickname = str()
        self.sessionKey = str()
        self.sex = int()

    def _read(self, _is):
        self.userId = _is.readInt()
        self.username = _is.readString()
        self.nickname = _is.readString()
        self.sessionKey = _is.readString()
        self.sex = _is.readInt()

    def _write(self, _os):
        _os.writeInt(self.userId)
        _os.writeString(self.username)
        _os.writeString(self.nickname)
        _os.writeString(self.sessionKey)
        _os.writeInt(self.sex)

    def _fromJson(self, js):
        if 'userId' in js and isinstance(js['userId'], int):
            self.userId = js['userId']
        if 'username' in js and isinstance(js['username'], str):
            self.username = js['username']
        if 'nickname' in js and isinstance(js['nickname'], str):
            self.nickname = js['nickname']
        if 'sessionKey' in js and isinstance(js['sessionKey'], str):
            self.sessionKey = js['sessionKey']
        if 'sex' in js and isinstance(js['sex'], int):
            self.sex = js['sex']

    def _toJson(self):
        js = dict()
        js['userId'] = self.userId
        js['username'] = self.username
        js['nickname'] = self.nickname
        js['sessionKey'] = self.sessionKey
        js['sex'] = self.sex
        return js

MessageBlock.register(SLoginReturn)

class SMessage:
    def __init__(self):
        self.var1 = int()
        self.var2 = int()
        self.var3 = int()
        self.var4 = float()
        self.var5 = float()
        self.var6 = str()
        self.var7 = datetime.datetime.now()
        self.intList = []
        self.dictStrInt = {}

    def _read(self, _is):
        self.var1 = _is.readShort()
        self.var2 = _is.readInt()
        self.var3 = _is.readLong()
        self.var4 = _is.readFloat()
        self.var5 = _is.readDouble()
        self.var6 = _is.readString()
        self.var7 = _is.readDate()
        message.common.publicdef.readSeqInt(_is, self.intList)
        message.common.publicdef.readDictStringInt(_is, self.dictStrInt)

    def _write(self, _os):
        _os.writeShort(self.var1)
        _os.writeInt(self.var2)
        _os.writeLong(self.var3)
        _os.writeFloat(self.var4)
        _os.writeDouble(self.var5)
        _os.writeString(self.var6)
        _os.writeDate(self.var7)
        message.common.publicdef.writeSeqInt(_os, self.intList)
        message.common.publicdef.writeDictStringInt(_os, self.dictStrInt)

    def _fromJson(self, js):
        if 'var1' in js and isinstance(js['var1'], int):
            self.var1 = js['var1']
        if 'var2' in js and isinstance(js['var2'], int):
            self.var2 = js['var2']
        if 'var3' in js and isinstance(js['var3'], int):
            self.var3 = js['var3']
        if 'var4' in js and isinstance(js['var4'], float):
            self.var4 = js['var4']
        if 'var5' in js and isinstance(js['var5'], float):
            self.var5 = js['var5']
        if 'var6' in js and isinstance(js['var6'], str):
            self.var6 = js['var6']
        if 'var7' in js and isinstance(js['var7'], datetime.datetime):
            self.var7 = js['var7']
        if 'intList' in js and isinstance(js['intList'], list):
            self.intList = message.common.publicdef.SeqIntFromJson(js['intList'])
        if 'dictStrInt' in js and isinstance(js['dictStrInt'], dict):
            self.dictStrInt = message.common.publicdef.DictStringIntFromJson(js['dictStrInt'])

    def _toJson(self):
        js = dict()
        js['var1'] = self.var1
        js['var2'] = self.var2
        js['var3'] = self.var3
        js['var4'] = self.var4
        js['var5'] = self.var5
        js['var6'] = self.var6
        js['var7'] = self.var7
        js['intList'] = message.common.publicdef.SeqIntToJson(self.intList)
        js['dictStrInt'] = message.common.publicdef.DictStringIntToJson(self.dictStrInt)
        return js

MessageBlock.register(SMessage)

def readDictMessage(_is, valDict):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        key_ = int()
        val_ = SMessage()
        key_ = _is.readInt()
        val_._read(_is)
        valDict[key_] = val_

def writeDictMessage(_os, valDict):
    dataSize = len(valDict)
    _os.writeInt(dataSize)
    for item in valDict.items():
        _os.writeInt(item[0])
        item[1]._write(_os)

def DictMessageFromJson(js):
    res = dict()
    for key_ in js:
        val = SMessage()
        val._fromJson(js[key_])
        res[key_] = val
    return res

def DictMessageToJson(valDict):
    res = dict()
    for key_ in valDict:
        res[key_] = valDict[key_]._toJson()
    return res

