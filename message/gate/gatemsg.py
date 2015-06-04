#
# file: gatemsg.py
#
# date: 2015-06-04 16:19:16.876546
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

    def __read(self, __is):
        self.username = __is.readString()
        self.nickname = __is.readString()
        self.password = __is.readString()
        self.sex = __is.readInt()

    def __write(self, __os):
        __os.writeString(self.username)
        __os.writeString(self.nickname)
        __os.writeString(self.password)
        __os.writeInt(self.sex)

MessageBlock.register(SSignup)

class SLogin:
    def __init__(self):
        self.username = str()
        self.password = str()

    def __read(self, __is):
        self.username = __is.readString()
        self.password = __is.readString()

    def __write(self, __os):
        __os.writeString(self.username)
        __os.writeString(self.password)

MessageBlock.register(SLogin)

class SLoginReturn:
    def __init__(self):
        self.userId = int()
        self.username = str()
        self.nickname = str()
        self.sessionKey = str()
        self.sex = int()

    def __read(self, __is):
        self.userId = __is.readInt()
        self.username = __is.readString()
        self.nickname = __is.readString()
        self.sessionKey = __is.readString()
        self.sex = __is.readInt()

    def __write(self, __os):
        __os.writeInt(self.userId)
        __os.writeString(self.username)
        __os.writeString(self.nickname)
        __os.writeString(self.sessionKey)
        __os.writeInt(self.sex)

MessageBlock.register(SLoginReturn)

class SMessage:
    def __init__(self):
        self.var1 = int()
        self.var2 = int()
        self.var3 = int()
        self.var4 = float()
        self.var5 = float()
        self.var6 = str()
        self.var7 = datetime.datetime()

    def __read(self, __is):
        self.var1 = __is.readShort()
        self.var2 = __is.readInt()
        self.var3 = __is.readLong()
        self.var4 = __is.readFloat()
        self.var5 = __is.readDouble()
        self.var6 = __is.readString()
        self.var7 = __is.readDate()

    def __write(self, __os):
        __os.writeShort(self.var1)
        __os.writeInt(self.var2)
        __os.writeLong(self.var3)
        __os.writeFloat(self.var4)
        __os.writeDouble(self.var5)
        __os.writeString(self.var6)
        __os.writeDate(self.var7)

MessageBlock.register(SMessage)

