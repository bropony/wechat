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
    @classmethod
    def isBasice(cls):
        return False

class BasicType(RmiType):
    @classmethod
    def getPyInit(cls, name):
        return "{} = {}()".format(name, cls.__name)

    @classmethod
    def getPyRead(cls, name):
        return "{} = __is.read{}()".format(name, cls.__name.capitalize())

    @classmethod
    def getPyWrite(cls, name):
        return  "__os.write{}({})".format(cls.__name.capitalize(), name)

    @classmethod
    def isBasic(cls):
        return  True

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


class __Sequence(RmiType):
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def getPyInit(self):
        return "{} = []".format(self.name)

    def getPyRead(self, scope):
        return "{0}.read{1}(__is, {1})".format(scope, self.name)

    def getPyWrite(self, scope):
        return "{0}.write{1}(__os, {1})".format(scope, self.name)

def sequence(type, name):
    obj = __Sequence(type, name)
