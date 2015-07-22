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
from gamit.serialize.util import *
import message.common.publicdef
import message.gate.command


class SeqSeqInt(ListBase):
    def __init__(self):
        super().__init__(message.common.publicdef.SeqInt, 'SeqSeqInt')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = message.common.publicdef.SeqInt()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = message.common.publicdef.SeqInt()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

class SeqDictIntInt(ListBase):
    def __init__(self):
        super().__init__(message.common.publicdef.DictIntInt, 'SeqDictIntInt')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = message.common.publicdef.DictIntInt()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = message.common.publicdef.DictIntInt()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

class DictDictStringInt(DictBase):
    def __init__(self):
        super().__init__(int, message.common.publicdef.DictStringInt, 'DictDictStringInt')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = int()
            val_ = message.common.publicdef.DictStringInt()
            key_ = _is.readInt()
            val_._read(_is)
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeInt(item[0])
            item[1]._write(_os)

    def _fromJson(self, js):
        for key_ in js:
            val = message.common.publicdef.DictStringInt()
            val._fromJson(js[key_])
            self[key_] = val

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]._toJson()
        return res

class SSignup:
    __slots__ = dict()
    __slots__['username'] = str
    __slots__['nickname'] = str
    __slots__['password'] = str
    __slots__['sex'] = int

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SSignup.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

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
    __slots__ = dict()
    __slots__['username'] = str
    __slots__['password'] = str

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SLogin.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

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
    __slots__ = dict()
    __slots__['userId'] = int
    __slots__['username'] = str
    __slots__['nickname'] = str
    __slots__['sessionKey'] = str
    __slots__['sex'] = int

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SLoginReturn.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

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
    __slots__ = dict()
    __slots__['var1'] = int
    __slots__['var2'] = int
    __slots__['var3'] = int
    __slots__['var4'] = float
    __slots__['var5'] = float
    __slots__['var6'] = str
    __slots__['var7'] = datetime.datetime
    __slots__['intList'] = message.common.publicdef.SeqInt
    __slots__['dictStrInt'] = message.common.publicdef.DictStringInt
    __slots__['commandType'] = int

    def __setattr__(self, name, val):
        if name in self.__slots__ and not isinstance(val, self.__slots__[name]):
            clsName = self.__slots__[name].__name__
            raise Exception('Value of SMessage.' + name + ' must be ' + clsName + ' object')

        object.__setattr__(self, name, val)

    def __getitem__(self, key):
        return object.__getattribute__(self, key)

    def __init__(self):
        self.var1 = int()
        self.var2 = int()
        self.var3 = int()
        self.var4 = float()
        self.var5 = float()
        self.var6 = str()
        self.var7 = datetime.datetime.now()
        self.intList = message.common.publicdef.SeqInt()
        self.dictStrInt = message.common.publicdef.DictStringInt()
        self.commandType = message.gate.command.ETestCommand.FirstMessage

    def _read(self, _is):
        self.var1 = _is.readShort()
        self.var2 = _is.readInt()
        self.var3 = _is.readLong()
        self.var4 = _is.readFloat()
        self.var5 = _is.readDouble()
        self.var6 = _is.readString()
        self.var7 = _is.readDate()
        self.intList._read(_is)
        self.dictStrInt._read(_is)
        self.commandType = _is.readInt()

    def _write(self, _os):
        _os.writeShort(self.var1)
        _os.writeInt(self.var2)
        _os.writeLong(self.var3)
        _os.writeFloat(self.var4)
        _os.writeDouble(self.var5)
        _os.writeString(self.var6)
        _os.writeDate(self.var7)
        self.intList._write(_os)
        self.dictStrInt._write(_os)
        _os.writeInt(self.commandType)

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
        elif 'var7' in js and isinstance(self.var7, datetime.datetime):
            self.var7 = datetime.datetime.strptime(js['var7'], '%Y-%m-%d %H:%M:%S')
        if 'intList' in js and isinstance(js['intList'], message.common.publicdef.SeqInt):
            self.intList._fromJson(js['intList'])
        elif 'intList' in js and isinstance(js['intList'], list):
            self.intList._fromJson(js['intList'])
        if 'dictStrInt' in js and isinstance(js['dictStrInt'], message.common.publicdef.DictStringInt):
            self.dictStrInt._fromJson(js['dictStrInt'])
        elif 'dictStrInt' in js and isinstance(js['dictStrInt'], dict):
            self.dictStrInt._fromJson(js['dictStrInt'])
        if 'commandType' in js and isinstance(js['commandType'], int):
            self.commandType = js['commandType']

    def _toJson(self):
        js = dict()
        js['var1'] = self.var1
        js['var2'] = self.var2
        js['var3'] = self.var3
        js['var4'] = self.var4
        js['var5'] = self.var5
        js['var6'] = self.var6
        js['var7'] = self.var7
        js['intList'] = self.intList._toJson()
        js['dictStrInt'] = self.dictStrInt._toJson()
        js['commandType'] = self.commandType
        return js

MessageBlock.register(SMessage)

class SeqMessage(ListBase):
    def __init__(self):
        super().__init__(SMessage, 'SeqMessage')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = SMessage()
            val._read(_is)
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            val._write(_os)

    def _fromJson(self, js):
        for js_c in js:
            val = SMessage()
            val._fromJson(js_c)
            self.append(val)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val._toJson())
        return res

class DictMessage(DictBase):
    def __init__(self):
        super().__init__(int, SMessage, 'DictMessage')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = int()
            val_ = SMessage()
            key_ = _is.readInt()
            val_._read(_is)
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeInt(item[0])
            item[1]._write(_os)

    def _fromJson(self, js):
        for key_ in js:
            val = SMessage()
            val._fromJson(js[key_])
            self[key_] = val

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]._toJson()
        return res

