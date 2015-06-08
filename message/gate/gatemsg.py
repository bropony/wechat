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

    def _read(self, _is):
        self.var1 = _is.readShort()
        self.var2 = _is.readInt()
        self.var3 = _is.readLong()
        self.var4 = _is.readFloat()
        self.var5 = _is.readDouble()
        self.var6 = _is.readString()
        self.var7 = _is.readDate()
        message.common.publicdef.readSeqInt(_is, self.intList)

    def _write(self, _os):
        _os.writeShort(self.var1)
        _os.writeInt(self.var2)
        _os.writeLong(self.var3)
        _os.writeFloat(self.var4)
        _os.writeDouble(self.var5)
        _os.writeString(self.var6)
        _os.writeDate(self.var7)
        message.common.publicdef.writeSeqInt(_os, self.intList)

MessageBlock.register(SMessage)

