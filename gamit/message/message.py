__author__ = 'mahanzhou'

from gamit.serialize.serializer import Serializer
from  gamit.serialize.datatype import RmiDataType

class MessageRegisteredError(Exception):
    pass

class MessageNotRegisteredError(Exception):
    pass

class MessageBlock:
    __msgMap = {}

    @classmethod
    def register(cls, messageType):
        #if messageType.__name__ in cls.__msgMap:
        #    raise MessageRegisteredError()
        #
        cls.__msgMap[messageType.__name__] = messageType

    def __init__(self, dataType, toIdList=None, data=None):
        if isinstance(dataType, int):
            self.command = dataType
            self.toIdList = toIdList
            self.data = data
            self.__os = Serializer()
            self.__write()
        else:
            self.__is = dataType
            self.__read()

    def __read(self):
        self.command = self.__is.readInt() # 1 command
        self.toIdList = []
        idSize = self.__is.readInt()       # 2 toIdList
        for dummy in range(0, idSize):
            id = self.__is.readInt()
            self.toIdList.append(id)
        name = self.__is.readString()      # 3 message name
        if name not in self.__msgMap:
            raise MessageNotRegisteredError()
        self.data = self.__msgMap[name]()  # 4 data
        self.data.read__(self.__is)

    def __write(self):
        self.__os.startToWrite()
        self.__os.writeByte(RmiDataType.MessageBlock)
        self.__os.writeInt(self.command)  # 1 command
        idSize = len(self.toIdList)       # 2 toIdList
        self.__os.writeInt(idSize)
        for id in self.toIdList:
            self.__os.writeInt(id)
        self.__os.writeString(self.data.__class__.__name__) # 3 message name
        self.data.write__(self.__os)      # 4 data

    def getOsBuffer(self):
        return self.__os.getBuffer()

