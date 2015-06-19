"""
* @name util.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/15 16:41
*
* @desc util.py
"""

class ListBase(list):
    def __init__(self, valType, name):
        self.valType = valType
        self.name = name
        self.typeError = "Element value of {} must be {} object".format(name, valType.__name__)

    def checkValType(self, val):
        if not isinstance(val, self.valType):
            raise Exception(self.typeError, 0)

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            for val in value:
                self.checkValType(val)
        else:
            self.checkValType(value)

        super().__setitem__(key, value)

    def append(self, value):
        self.checkValType(value)

        super().append(value)

    def insert(self, index, value):
        self.checkValType(value)

        super().insert(index, value)

class DictBase(dict):
    def __init__(self, keyType, valType, name):
        self.keyType = keyType
        self.valType = valType
        self.name = name

        self.keyTypeError = "Key of {} must be {} object".format(name, keyType.__name__)
        self.valTypeError = "Value of {} must be {} object".format(name, valType.__name__)

    def checkKeyType(self, key):
        if not isinstance(key, self.keyType):
            raise Exception(self.keyTypeError, 0)

    def checkValType(self, val):
        if not isinstance(val, self.valType):
            raise Exception(self.valTypeError, 0)

    def __setitem__(self, key, value):
        self.checkKeyType(key)
        self.checkValType(value)

        super().__setitem__(key, value)

    def update(self, E=None, **F):
        if isinstance(E, dict):
            for key, value in self.items():
                self.checkKeyType(key)
                self.checkValType(value)

        super().update(E, **F)

    def setdefault(self, k, d):
        self.checkKeyType(k)
        self.checkValType(d)

        super().setdefault(k, d)

    def get(self, k, d=None):
        if not k in self:
            if not d:
                return self.valType()

        return super().get(k, d)
