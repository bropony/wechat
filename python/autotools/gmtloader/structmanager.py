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
        self.loadedMap = {}

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
        if relPath in self.loadedMap:
            return self.loadedMap[relPath]

        loader = Loader(self.baseScope, self.inRootDir, relPath, self)
        loader.loadFile()
        self.loadedMap[relPath] = loader

        return loader

    def find(self, name, scope=""):
        if name in self.typeMap:
            return self.typeMap[name]

        if not scope:
            return None

        newName = scope + "." + name
        if newName in self.typeMap:
            return self.typeMap[newName]
        #else:
        #    print("type not found:", newName)

        parent_scopes = re.split(r'\.', scope)
        child_scopes = re.split(r'\.', name)
        depth_parent = len(parent_scopes)
        depth_child = len(child_scopes)
        if depth_child <= 1:
            return None

        if depth_parent < depth_child:
            return None

        for i in range(depth_child - 1):
            child_idx = -2 - i
            parent_idx = -1 - i
            parent_scopes[parent_idx] = child_scopes[child_idx]

        parent_scopes.append(child_scopes[-1])
        newName = ".".join(parent_scopes)
        if newName in self.typeMap:
            return self.typeMap[newName]
        #else:
            #print("Type Not Found:", newName)

        return None

    def add(self, dataType):
        self.typeMap[dataType.fullname] = dataType
        #print("[StructManager.add]", dataType.fullname)
# end of StructManager
