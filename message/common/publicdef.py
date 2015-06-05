#
# file: publicdef.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock


def readSeqInt(_is, valList):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        val = int()
        val = _is.readInt()
        valList.append(val)

def writeSeqInt(_os, valList):
    dataSize = len(valList)
    _os.writeInt(dataSize)
    for val in valList:
        _os.writeInt(val)

def readSeqLong(_is, valList):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        val = int()
        val = _is.readLong()
        valList.append(val)

def writeSeqLong(_os, valList):
    dataSize = len(valList)
    _os.writeInt(dataSize)
    for val in valList:
        _os.writeLong(val)

def readSeqString(_is, valList):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        val = str()
        val = _is.readString()
        valList.append(val)

def writeSeqString(_os, valList):
    dataSize = len(valList)
    _os.writeInt(dataSize)
    for val in valList:
        _os.writeString(val)

def readSeqFloat(_is, valList):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        val = float()
        val = _is.readFloat()
        valList.append(val)

def writeSeqFloat(_os, valList):
    dataSize = len(valList)
    _os.writeInt(dataSize)
    for val in valList:
        _os.writeFloat(val)

def readDictIntInt(_is, valDict):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        key_ = int()
        val_ = int()
        key_ = _is.readInt()
        val_ = _is.readInt()
        valDict[key_] = val_

def writeDictIntInt(_os, valDict):
    dataSize = len(valDict)
    _os.writeInt(dataSize)
    for item in valDict.items():
        _os.writeInt(item[0])
        _os.writeInt(item[1])

def readDictIntString(_is, valDict):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        key_ = int()
        val_ = str()
        key_ = _is.readInt()
        val_ = _is.readString()
        valDict[key_] = val_

def writeDictIntString(_os, valDict):
    dataSize = len(valDict)
    _os.writeInt(dataSize)
    for item in valDict.items():
        _os.writeInt(item[0])
        _os.writeString(item[1])

def readDictStringInt(_is, valDict):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        key_ = str()
        val_ = int()
        key_ = _is.readString()
        val_ = _is.readInt()
        valDict[key_] = val_

def writeDictStringInt(_os, valDict):
    dataSize = len(valDict)
    _os.writeInt(dataSize)
    for item in valDict.items():
        _os.writeString(item[0])
        _os.writeInt(item[1])

def readDictStringString(_is, valDict):
    dataSize = _is.readInt()
    for _ in range(dataSize):
        key_ = str()
        val_ = str()
        key_ = _is.readString()
        val_ = _is.readString()
        valDict[key_] = val_

def writeDictStringString(_os, valDict):
    dataSize = len(valDict)
    _os.writeInt(dataSize)
    for item in valDict.items():
        _os.writeString(item[0])
        _os.writeString(item[1])

