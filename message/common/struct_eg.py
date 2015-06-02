#
# file: struct_eg.py
#
# date: 2015-06-02 16:18:10.629722
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock


def readSeqInt(__is, valList):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        val = int()
        val = __is.readInt()
        valList.append(val)

def writeSeqInt(__os, valList):
    dataSize = len(valList)
    __os.writeInt(dataSize)
    for val in valList:
        __os.writeInt(val)

def readDictIntString(__is, valDict):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        key_ = int()
        val_ = str()
        key_ = __is.readInt()
        val_ = __is.readString()
        valDict[key_] = val_

def writeDictIntString(__os, valDict):
    dataSize = len(valDict)
    __os.writeInt(dataSize)
    for item in valDict.items():
        __os.writeInt(item[0])
        __os.writeString(item[1])

class SAddress:
    def __init__(self):
        self.code = int()
        self.city = str()
        self.district = str()
        self.details = str()

    def __read(self, __is):
        self.code = __is.readInt()
        self.city = __is.readString()
        self.district = __is.readString()
        self.details = __is.readString()

    def __write(self, __os):
        __os.writeInt(self.code)
        __os.writeString(self.city)
        __os.writeString(self.district)
        __os.writeString(self.details)

MessageBlock.register(SAddress)

class SHuman:
    def __init__(self):
        self.age = int()
        self.name = str()
        self.address = SAddress()
        self.hobbies = []

    def __read(self, __is):
        self.age = __is.readInt()
        self.name = __is.readString()
        self.address.__read(__is)
        readSeqInt(__is, self.hobbies)

    def __write(self, __os):
        __os.writeInt(self.age)
        __os.writeString(self.name)
        self.address.__write(__os)
        writeSeqInt(__os, self.hobbies)

MessageBlock.register(SHuman)

def readSeqHuman(__is, valList):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        val = SHuman()
        val.__read(__is)
        valList.append(val)

def writeSeqHuman(__os, valList):
    dataSize = len(valList)
    __os.writeInt(dataSize)
    for val in valList:
        val.__write(__os)

class ETest:
    hello = 1
    world = 2

