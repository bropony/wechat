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


SeqInt = list

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

def SeqIntFromJson(js):
    return js

def SeqIntToJson(valList):
    return valList

SeqLong = list

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

def SeqLongFromJson(js):
    return js

def SeqLongToJson(valList):
    return valList

SeqString = list

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

def SeqStringFromJson(js):
    return js

def SeqStringToJson(valList):
    return valList

SeqFloat = list

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

def SeqFloatFromJson(js):
    return js

def SeqFloatToJson(valList):
    return valList

DictIntInt = dict

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

def DictIntIntFromJson(js):
    return js

def DictIntIntToJson(valDict):
    return valDict

DictIntString = dict

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

def DictIntStringFromJson(js):
    return js

def DictIntStringToJson(valDict):
    return valDict

DictStringInt = dict

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

def DictStringIntFromJson(js):
    return js

def DictStringIntToJson(valDict):
    return valDict

DictStringString = dict

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

def DictStringStringFromJson(js):
    return js

def DictStringStringToJson(valDict):
    return valDict

