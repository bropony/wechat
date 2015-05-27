"""
* @name loader.py
*
* @author ahda86@gmail.com
*
* @date 2015/5/27 20:02
*
* @desc loader.py
"""

class TypeBase:
    def __init__(self, scope, name):
        self.scope = scope
        self.name = name
        self.fullname = scope + "." + name


class DataType(TypeBase):
    def __init__(self, scope, name, type, isBasic):
        super().__init__(scope, name)
        self.type = type
        self.isBasic = isBasic

    def parse(self, lines):
        pass


class Enum(TypeBase):
    def __init__(self, scope, name):
        super().__init__(scope, name)

    def parse(self, lines):
        pass


class List(TypeBase):
    def __init__(self, scope, name, type):
        super().__init__(scope, name)
        self.type = type

    def parse(self, lines):
        pass

class Dict(TypeBase):
    def __init__(self, scope, name, keyType, valType):
        super().__init__(scope, name)
        self.keyType = keyType
        self.valType = valType

    def parse(self):
        pass

class Interface(TypeBase):
    def __init__(self, scope, name):
        super().__init__(scope, name)
        self.methodList = []

    def addMethod(self, name, lines):
        pass

