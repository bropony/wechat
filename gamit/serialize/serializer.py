#
# @date 2015-04-15
#
# @author ahda86@gmail.com
#
# @desc class Serializer for serializing data
#

from gamit.serialize.version import VERSION

import struct
from datetime import datetime
#
# serializing error
#
class SerializeError(Exception):
    def __init__(self, what):
        super().__init__("SerializeError", what)
        self.what = what



class Serializer:
    #ctor
    def __init__(self, src = None):
        if isinstance(src, bytes):
            self._buffer = bytearray(src)
        elif isinstance(src, bytearray):
            self._buffer = bytearray(src)
        elif src == None:
            self._buffer = bytearray()
        else:
            raise SerializeError("instance of bytes or bytearray expected")
        
        self._offset = 0

    def getBuffer(self):
        return self._buffer

    #start to read
    def startToRead(self):
        ver = self.readByte()
        if ver != VERSION:
            print("Version Not Matched")
            raise SerializeError("Version Not Matched")

    #start to write
    def startToWrite(self):
        self.writeByte(VERSION)

    #_read
    def _read(self, fmt, size):
        res = struct.unpack_from(fmt, self._buffer, self._offset)
        self._offset += size

        return res[0]
    
    #_write
    def _write(self, fmt, data):
        b = struct.pack(fmt, data)
        self._buffer.extend(b)

    #read a byte
    def readByte(self):
        return self._read("b", 1)

    #write a byte
    def writeByte(self, b):
        self._write("b", b)

    #read a bool
    def readBool(self):
        b = self.readByte()
        b = (b != 0)
        return b

    #write a bool
    def writeBool(self, b):
        b = 1 if b else 0
        self.writeByte(b)

    #read a short
    def readShort(self):
        return self._read("<h", 2)

    #write a short
    def writeShort(self, s):
        self._write("<h", s)

    #read an int
    def readInt(self):
        return self._read("<i", 4)

    #write an int
    def writeInt(self, i):
        self._write("<i", i)

    #read a long
    def readLong(self):
        return self._read("<q", 8)

    #write a long
    def writeLong(self, l):
        self._write("<q", l)

    #read a float
    def readFloat(self):
        return self._read("<f", 4)

    #write a float
    def writeFloat(self, f):
        self._write("<f", f)

    #read a double
    def readDouble(self):
        return self._read("<d", 8)

    #write a double
    def writeDouble(self, d):
        self._write("<d", d)

    #read a string
    def readString(self):
        size = self.readInt()
        fmt = "{}s".format(size)
        bs = self._read(fmt, size)
        return bs.decode("utf-8")

    #write a string
    def writeString(self, s):
        s = s.encode("utf-8")
        size = len(s)
        self.writeInt(size)
        fmt = "{}s".format(size)
        self._write(fmt, s)

    #read a datetime
    def readDate(self):
        l = self.readLong();
        dt = datetime.fromtimestamp(l)
        return dt

    #write a datetime
    def writeDate(self, dt):
        l = dt.timestamp()
        self.writeLong(int(l))

    #read binary
    def readBinary(self):
        size = self.readInt()
        bb = bytes(self._buffer[self._offset : self._offset + size])
        self._offset += size

        return bb

    #write binary
    def writeBinary(self, bb):
        size = len(bb)
        self.writeInt(size)
        self._buffer.extend(bb)

    #encrypt
    def encrypt(self):
        mask = 108

        buffSize = len(self._buffer)
        if buffSize == 0:
            return

        maxIdx = buffSize - 1
        for i in range(0, buffSize, 2):
            if i == maxIdx:
                self._buffer[i] ^= mask
                return

            bi = self._buffer[i]
            bj = self._buffer[i + 1]

            bi ^= mask
            bj ^= mask

            self._buffer[i] = bj
            self._buffer[i + 1] = bi

    #decrypt
    def decrypt(self):
        self.encrypt()

