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
from gamit.serialize.util import *


class SeqInt(ListBase):
    def __init__(self):
        super().__init__(int, 'SeqInt')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = int()
            val = _is.readInt()
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            _os.writeInt(val)

    def _fromJson(self, js):
        for js_c in js:
            self.append(js_c)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val)
        return res

class SeqLong(ListBase):
    def __init__(self):
        super().__init__(int, 'SeqLong')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = int()
            val = _is.readLong()
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            _os.writeLong(val)

    def _fromJson(self, js):
        for js_c in js:
            self.append(js_c)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val)
        return res

class SeqString(ListBase):
    def __init__(self):
        super().__init__(str, 'SeqString')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = str()
            val = _is.readString()
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            _os.writeString(val)

    def _fromJson(self, js):
        for js_c in js:
            self.append(js_c)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val)
        return res

class SeqFloat(ListBase):
    def __init__(self):
        super().__init__(float, 'SeqFloat')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            val = float()
            val = _is.readFloat()
            self.append(val)

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for val in self:
            _os.writeFloat(val)

    def _fromJson(self, js):
        for js_c in js:
            self.append(js_c)

    def _toJson(self):
        res = []
        for val in self:
            res.append(val)
        return res

class DictIntInt(DictBase):
    def __init__(self):
        super().__init__(int, int, 'DictIntInt')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = int()
            val_ = int()
            key_ = _is.readInt()
            val_ = _is.readInt()
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeInt(item[0])
            _os.writeInt(item[1])

    def _fromJson(self, js):
        for key_ in js:
            self[key_] = js[key_] 

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]
        return res

class DictIntString(DictBase):
    def __init__(self):
        super().__init__(int, str, 'DictIntString')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = int()
            val_ = str()
            key_ = _is.readInt()
            val_ = _is.readString()
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeInt(item[0])
            _os.writeString(item[1])

    def _fromJson(self, js):
        for key_ in js:
            self[key_] = js[key_] 

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]
        return res

class DictStringInt(DictBase):
    def __init__(self):
        super().__init__(str, int, 'DictStringInt')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = str()
            val_ = int()
            key_ = _is.readString()
            val_ = _is.readInt()
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeString(item[0])
            _os.writeInt(item[1])

    def _fromJson(self, js):
        for key_ in js:
            self[key_] = js[key_] 

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]
        return res

class DictStringString(DictBase):
    def __init__(self):
        super().__init__(str, str, 'DictStringString')

    def _read(self, _is):
        dataSize = _is.readInt()
        for _ in range(dataSize):
            key_ = str()
            val_ = str()
            key_ = _is.readString()
            val_ = _is.readString()
            self[key_] = val_

    def _write(self, _os):
        dataSize = len(self)
        _os.writeInt(dataSize)
        for item in self.items():
            _os.writeString(item[0])
            _os.writeString(item[1])

    def _fromJson(self, js):
        for key_ in js:
            self[key_] = js[key_] 

    def _toJson(self):
        res = dict()
        for key_ in self:
            res[key_] = self[key_]
        return res

