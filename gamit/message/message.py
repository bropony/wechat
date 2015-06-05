__author__ = 'mahanzhou'

from gamit.serialize.serializer import Serializer
from  gamit.serialize.datatype import RmiDataType

class MessageRegisteredError(Exception):
    pass

class MessageNotRegisteredError(Exception):
    pass

class MessageBlock:
    _msgMap = {}

    @classmethod
    def register(cls, messageType):
        #if messageType.__name__ in cls.__msgMap:
        #    raise MessageRegisteredError()
        #
        cls._msgMap[messageType.__name__] = messageType

    def __init__(self, dataType, toIdList=None, data=None):
        if isinstance(dataType, int):
            self.command = dataType
            self.toIdList = toIdList
            self.data = data
            self._os = Serializer()
            self._write()
        else:
            self._is = dataType
            self._read()

    def _read(self):
        self.command = self._is.readInt() # 1 command
        self.toIdList = []
        idSize = self._is.readInt()       # 2 toIdList
        for dummy in range(0, idSize):
            id = self._is.readInt()
            self.toIdList.append(id)
        name = self._is.readString()      # 3 message name
        if name not in self._msgMap:
            raise MessageNotRegisteredError()
        self.data = self._msgMap[name]()  # 4 data
        self.data._read(self._is)

    def _write(self):
        self._os.startToWrite()
        self._os.writeByte(RmiDataType.MessageBlock)
        self._os.writeInt(self.command)  # 1 command
        idSize = len(self.toIdList)       # 2 toIdList
        self._os.writeInt(idSize)
        for id in self.toIdList:
            self._os.writeInt(id)
        self._os.writeString(self.data.__class__.__name__) # 3 message name
        self.data._write(self._os)      # 4 data

    def getOsBuffer(self):
        return self._os.getBuffer()

