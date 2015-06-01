"""
* @name structmanager.py
*
* @author ahda86@gmail.com
*
* @date 2015/5/27 20:11
*
* @desc structmanager.py
"""

from gmtloader.loader import *
import datetime

class StructManager:
    def __init__(self, baseScope, inRootDir, outRootDir):
        self.baseScope = baseScope
        self.inRootDir = inRootDir
        self.outRootDir = outRootDir
        self.typeMap = {}
        self.initBasicTypes()

    def initBasicTypes(self):
        self.add(BasicType("bool", bool))
        self.add(BasicType("byte", int))
        self.add(BasicType("short", int))
        self.add(BasicType("int", int))
        self.add(BasicType("long", int))
        self.add(BasicType("float", float))
        self.add(BasicType("double", float))
        self.add(BasicType("string", str))
        self.add(BasicType("date", datetime.datetime))
        self.add(BasicType("binary", bytes))

    def loadFile(self, relPath):
        loader = Loader(self.baseScope, self.inRootDir, relPath, self)
        loader.loadFile()
        return loader

    def find(self, name, scope=""):
        if name in self.typeMap:
            return self.typeMap[name]

        newName = scope + "." + name
        if newName in self.typeMap:
            return self.typeMap[newName]
        return None

    def add(self, dataType):
        self.typeMap[dataType.fullname] = dataType
        print("[StructManager.add]", dataType.fullname)
# end of StructManager
