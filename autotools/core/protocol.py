#
# protocols for declaration rmi data struct and interface
#

import datetime
from collections import OrderedDict
#
# meter classs that makes sure class member a list in their declaration order.
#
class __OrderedMeta__(type):
    @classmethod
    def __prepare__(metacls, name, bases): 
        return OrderedDict()

    def __new__(cls, name, bases, clsdict):
        c = type.__new__(cls, name, bases, clsdict)
        c._orderedKeys = clsdict.keys()
        return c

class RmiType(metaclass=__OrderedMeta__):
    def __init__(self, name, type, isbasic):
        self.__name = name
        self.__type = type
        self.__isbasic = isbasic
        

class BasicType(RmiType):
    def __init__(self, name, type):
         super().__init__(name, type, True)

class Bool(BasicType):
    __name = "bool"
    __type = bool

class Byte(BasicType):
    __name = "byte"
    __type = int

class Short(BasicType):
    __name = "short"
    __type = int

class Int(BasicType):
    __name = "int"
    __type = int

class Long(BasicType):
    __name = "long"
    __type = int

class Float(BasicType):
    __name = "float"
    __type = float

class Double(BasicType):
    __name = "double"
    __type = float

class String(BasicType):
    __name = "string"
    __type = str

class Date(BasicType):
    __name = "date"
    __type = datetime.datetime

class Binary(BasicType):
    __name = "binary"
    __type = bytes


class Struct(RmiType):
    def __init__(self, name, type):
        super().__init__(name, type, False)


class Sequence(RmiType):
    def __init__(self):
        pass
