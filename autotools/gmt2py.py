"""
* @name gmt2py
*
* @author ahda86@gmail.com
*
* @date 2015/5/29 14:36
*
* @desc gmt2py
"""
import sys
import os.path
import re
import datetime
from optparse import OptionParser

from gmtloader.loader import *
from gmtloader.structmanager import StructManager

class Gmt2Py:
    @staticmethod
    def raiseExcept(what):
        raise Exception(what)

    @staticmethod
    def getIndent(level):
        if level <= 0:
            return ""
        return "    " * level

    def __init__(self, manger, loader):
        self.structManager = manger
        self.loader = loader
        self.indent = 0
        self.fout = None

    def makedir(self, rootDir, scope):
        if not os.path.exists(rootDir):
            self.raiseExcept("outdir {} does not exist".format(rootDir))

        packages = re.split(r'\.', scope)
        print("makedir", scope, packages)
        currentPath = rootDir
        for pkg in packages[:-1]:
            currentPath = os.path.join(currentPath, pkg)
            if not os.path.exists(currentPath):
                os.mkdir(currentPath)
            pkgFile = os.path.join(currentPath, "__init__.py")
            if not os.path.exists(pkgFile):
                fInit = open(pkgFile, "w")
                fInit.write("#\n# pakage {}\n# Date {}\n#\n".format(pkg, datetime.datetime.now()))
                fInit.close()

        return os.path.join(currentPath, packages[-1] + ".py")

    def write(self, content, writeLine=True):
        self.fout.write(self.getIndent(self.indent))
        self.fout.write(content)
        if writeLine:
            self.fout.write("\n")

    def writeEmptyLine(self):
        self.fout.write("\n")

    def generate(self):
        print("Generation Python code of {}".format(self.loader.filepath))
        outRootDir = self.structManager.outRootDir
        scope = self.loader.scope
        pyFilePath = self.makedir(outRootDir, scope)

        self.fout = open(pyFilePath, "w")

        self.parseHeader(pyFilePath)
        self.parseImports()

        for dataType in self.loader.types:
            if isinstance(dataType, Struct):
                self.parseStruct(dataType)
            elif isinstance(dataType, Enum):
                self.parseEnum(dataType)
            elif isinstance(dataType, List):
                self.parseList(dataType)
            elif isinstance(dataType, Dict):
                self.parseDict(dataType)
            elif isinstance(dataType, Interface):
                self.parseInterface(dataType)
            else:
                self.raiseExcept("Unexpected datatype {}".format(type(dataType)))

        self.fout.close()

    def parseHeader(self, pyFilePath):
        self.write("#")
        self.write("# file: {}".format(os.path.split(pyFilePath)[-1]))
        self.write("#")
        self.write("# date: {}".format(datetime.datetime.now()))
        self.write("#")
        self.write("# author: ahda86@gmail.com")
        self.write("#")
        self.write("# CAUTION: This file is Auto-Generated.")
        self.write("# Please DON'T modify this file EVEN if you know what you are doing.")
        self.write("#\n\n")

    def parseImports(self):
        self.write("import datetime")
        self.write("from gamit.message.message import MessageBlock")
        if self.loader.hasInterface:
            self.write("from gamit.rmi.rmicore import *")

        for imp in self.loader.includes:
            self.write("import {}".format(imp))
        self.write("\n")

    @staticmethod
    def getTypePyName(dataType, currentScope):
        if isinstance(dataType, BasicType):
            if dataType.name != "date":
                return dataType.type.__name__
            else:
                return "datetime.datetime"
        else:
            if dataType.scope == currentScope:
                return dataType.name
            else:
                return dataType.fullname

    @classmethod
    def getTypePyInitExpression(cls, dataType, currentScope):
        if isinstance(dataType, Enum):
            if dataType.scope == currentScope:
                return "{}.{}".format(dataType.name, dataType.pairs[0][0])
            else:
                return "{}.{}".format(dataType.fullname, dataType.pairs[0][0])
        elif isinstance(dataType, Struct) or isinstance(dataType, BasicType):
            return cls.getTypePyName(dataType, currentScope) + "()"
        elif isinstance(dataType, List):
            return "[]"
        elif isinstance(dataType, Dict):
            return "{}"

    def getPyReadExpression(self, dataType, name, currentScope):
        res = "Oops"
        if isinstance(dataType, BasicType):
            res = "{} = __is.read{}()".format(name, dataType.name.capitalize())
        elif isinstance(dataType, Struct):
            res = "{}.__read(__is)".format(name)
        elif isinstance(dataType, List) or isinstance(dataType, Dict):
            if dataType.scope == currentScope:
                res = "read{}(__is, {})".format(dataType.name, name)
            else:
                res = "{}.read{}(__is, {})".format(dataType.scope, dataType.name, name)
        elif isinstance(dataType, Enum):
            res = "{} = __is.readInt()".format(name)

        return res

    def getPyWriteExpression(self, dataTye, name, currentScope):
        res = "Oops"
        if isinstance(dataTye, BasicType):
            res = "__os.write{}({})".format(dataTye.name.capitalize(), name)
        elif isinstance(dataTye, Struct):
            res = "{}.__write(__os)".format(name)
        elif isinstance(dataTye, List) or isinstance(dataTye, Dict):
            if dataTye.scope == currentScope:
                res = "write{}(__os, {})".format(dataTye.name, name)
            else:
                res = "{}.write{}(__os, {})".format(dataTye.scope, dataTye.name, name)
        elif isinstance(dataTye, Enum):
            res = "__os.writeInt({})".format(name)

        return res

    def parseStruct(self, structType):
        self.indent = 0
        self.write("class {}:".format(structType.name))

        self.indent = 1
        self.write("def __init__(self):")
        self.indent = 2
        for field in structType.fields:
            fieldName = field.name
            initExpr = self.getTypePyInitExpression(field.type, self.loader.scope)
            self.write("self.{} = {}".format(fieldName, initExpr))
        self.writeEmptyLine()

        self.indent = 1
        self.write("def __read(self, __is):")
        self.indent = 2
        for field in structType.fields:
            fieldName = "self." + field.name
            expression = self.getPyReadExpression(field.type, fieldName, self.loader.scope)
            self.write(expression)
        self.writeEmptyLine()

        self.indent = 1
        self.write("def __write(self, __os):")
        self.indent = 2
        for field in structType.fields:
            fieldName = "self." + field.name
            expression = self.getPyWriteExpression(field.type, fieldName, self.loader.scope)
            self.write(expression)

        self.indent = 0
        self.writeEmptyLine()

    def parseEnum(self, enumType):
        self.indent = 0
        self.write("class {}:".format(enumType.name))

        self.indent = 1
        for pair in enumType.pairs:
            self.write("{} = {}".format(*pair))
        self.indent = 0
        self.writeEmptyLine()

    def parseList(self, listType):
        self.indent = 0
        #capName = listType.name.capitalize()
        capName = listType.name

        self.write("def read{}(__is, valList):".format(capName))
        self.indent = 1
        self.write("dataSize = __is.readInt()")
        self.write("for _ in range(dataSize):")
        self.indent = 2
        initExpr = self.getTypePyInitExpression(listType.type, self.loader.scope)
        self.write("val = {}".format(initExpr))
        readExp = self.getPyReadExpression(listType.type, "val", self.loader.scope)
        self.write(readExp)
        self.write("valList.append(val)")

        self.indent = 0
        self.writeEmptyLine()

        self.write("def write{}(__os, valList):".format(capName))
        self.indent = 1
        self.write("dataSize = len(valList)")
        self.write("__os.writeInt(dataSize)")
        self.write("for val in valList:")
        self.indent = 2
        writeExp = self.getPyWriteExpression(listType.type, "val", self.loader.scope)
        self.write(writeExp)

        self.indent = 0
        self.writeEmptyLine()

    def parseDict(self, dictType):
        self.indent = 0
        self.write("def read{}(__is, valDict):".format(dictType.name))
        self.indent = 1
        self.write("dataSize = __is.readInt()")
        self.write("for _ in range(dataSize):")
        self.indent = 2
        keyReadExpr = self.getPyReadExpression(dictType.keyType, "key_", self.loader.scope)
        valReadExpr = self.getPyReadExpression(dictType.valType, "val_", self.loader.scope)
        self.write(keyReadExpr)
        self.write(valReadExpr)
        self.write("valDict[key_] = val_")

        self.indent = 0
        self.writeEmptyLine()

        self.write("def write{}(__os, valDict):".format(dictType.name))
        self.indent = 1
        self.write("dataSize = len(valDict)")
        self.write("__os.writeInt(dataSize)")
        self.write("for item in valDict.items():")
        self.indent = 2
        keyWriteExpr = self.getPyWriteExpression(dictType.keyType, "item[0]", self.loader.scope)
        valWriteExpr = self.getPyWriteExpression(dictType.valType, "item[1]", self.loader.scope)
        self.write(keyWriteExpr)
        self.write(valWriteExpr)

        self.indent = 0
        self.writeEmptyLine()

    def parseInterface(self, interfaceType):
        pass

    def parseRmiRequest(self, interfaceType, method):
        pass

    def parseRmiResponse(self, interfaceType, method):
        pass

    def parseServant(self, interfaceType):
        pass

    def parseProxy(self, interfaceType):
        pass

def main():
    parser = OptionParser()
    parser.add_option("-n", "--namespace", help="root python module name",
                      dest="scope")
    parser.add_option("-g", "--gmt-dir", help="root directory of gmt files",
                      dest="inRootDir")
    parser.add_option("-o", "--out-dir", help="root directory of generated python files",
                      dest="outRootDir")
    parser.add_option("-f", "--file", dest="sources", action="append",
                      help="relative path of source gmt file. Multi-assignation is allowed.")
    #parser.add_option("-h","--help", help="show this message", action="store_false")

    options, args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return

    scope = options.scope or ""
    inRootDir = options.inRootDir or "."
    outRootDir = options.outRootDir or "."
    sources = options.sources or []

    if not sources:
        return

    structManager = StructManager(scope, inRootDir, outRootDir)
    loaders = []
    for f in sources:
        loader = structManager.loadFile(f)
        gmt = Gmt2Py(structManager, loader)
        gmt.generate()

if __name__ == "__main__":
    main()
