#
# file: publicdef.py
#
# date: 2015-06-04 16:19:16.868545
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

def readSeqLong(__is, valList):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        val = int()
        val = __is.readLong()
        valList.append(val)

def writeSeqLong(__os, valList):
    dataSize = len(valList)
    __os.writeInt(dataSize)
    for val in valList:
        __os.writeLong(val)

def readSeqString(__is, valList):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        val = str()
        val = __is.readString()
        valList.append(val)

def writeSeqString(__os, valList):
    dataSize = len(valList)
    __os.writeInt(dataSize)
    for val in valList:
        __os.writeString(val)

def readSeqFloat(__is, valList):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        val = float()
        val = __is.readFloat()
        valList.append(val)

def writeSeqFloat(__os, valList):
    dataSize = len(valList)
    __os.writeInt(dataSize)
    for val in valList:
        __os.writeFloat(val)

def readDictIntInt(__is, valDict):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        key_ = int()
        val_ = int()
        key_ = __is.readInt()
        val_ = __is.readInt()
        valDict[key_] = val_

def writeDictIntInt(__os, valDict):
    dataSize = len(valDict)
    __os.writeInt(dataSize)
    for item in valDict.items():
        __os.writeInt(item[0])
        __os.writeInt(item[1])

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

def readDictStringInt(__is, valDict):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        key_ = str()
        val_ = int()
        key_ = __is.readString()
        val_ = __is.readInt()
        valDict[key_] = val_

def writeDictStringInt(__os, valDict):
    dataSize = len(valDict)
    __os.writeInt(dataSize)
    for item in valDict.items():
        __os.writeString(item[0])
        __os.writeInt(item[1])

def readDictStringString(__is, valDict):
    dataSize = __is.readInt()
    for _ in range(dataSize):
        key_ = str()
        val_ = str()
        key_ = __is.readString()
        val_ = __is.readString()
        valDict[key_] = val_

def writeDictStringString(__os, valDict):
    dataSize = len(valDict)
    __os.writeInt(dataSize)
    for item in valDict.items():
        __os.writeString(item[0])
        __os.writeString(item[1])

