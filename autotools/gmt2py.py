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
        #print("makedir", scope, packages)
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
        print("Generation Python code for {}".format(self.loader.filepath))
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
        # self.write("#")
        # self.write("# date: {}".format(datetime.datetime.now()))
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
            self.write("from gamit.serialize.serializer import Serializer")
            self.write("from gamit.serialize.datatype import RmiDataType")
            self.write("import abc")

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
        elif isinstance(dataType, Enum):
            return "int"
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
        elif dataType.name == 'date':
            return "datetime.datetime.now()"
        elif isinstance(dataType, Struct) or isinstance(dataType, BasicType):
            return cls.getTypePyName(dataType, currentScope) + "()"
        elif isinstance(dataType, List):
            return "[]"
        elif isinstance(dataType, Dict):
            return "{}"

    def getPyReadExpression(self, dataType, name, currentScope):
        res = "Oops"
        if isinstance(dataType, BasicType):
            res = "{} = _is.read{}()".format(name, dataType.name.capitalize())
        elif isinstance(dataType, Struct):
            res = "{}._read(_is)".format(name)
        elif isinstance(dataType, List) or isinstance(dataType, Dict):
            if dataType.scope == currentScope:
                res = "read{}(_is, {})".format(dataType.name, name)
            else:
                res = "{}.read{}(_is, {})".format(dataType.scope, dataType.name, name)
        elif isinstance(dataType, Enum):
            res = "{} = _is.readInt()".format(name)

        return res

    def genJsonReadExpr(self, dataType, varExpr, varName, currentScope):
        dataTypeName = self.getTypePyName(dataType, currentScope)
        jsExpr = "js['{}']".format(varName)
        self.write("if '{}' in js and isinstance({}, {}):".format(varName, jsExpr, dataTypeName))
        self.indent += 1
        if isinstance(dataType, BasicType):
            self.write("{} = {}".format(varExpr, jsExpr))
        elif isinstance(dataType, Struct):
            self.write("{}._fromJson({})".format(varExpr, jsExpr))
        elif isinstance(dataType, List) or isinstance(dataType, Dict):
            if dataType.scope == currentScope:
                self.write("{}FromJson({}, {})".format(dataType.name, jsExpr, varExpr))
            else:
                self.write("{} = {}.{}FromJson({})".format(varExpr, dataType.scope, dataType.name, jsExpr))
        elif isinstance(dataType, Enum):
            self.write("{} = {}".format(varExpr, jsExpr))
        else:
            self.write("pass")
        self.indent -= 1

    def getPyWriteExpression(self, dataTye, name, currentScope):
        res = "Oops"
        if isinstance(dataTye, BasicType):
            res = "_os.write{}({})".format(dataTye.name.capitalize(), name)
        elif isinstance(dataTye, Struct):
            res = "{}._write(_os)".format(name)
        elif isinstance(dataTye, List) or isinstance(dataTye, Dict):
            if dataTye.scope == currentScope:
                res = "write{}(_os, {})".format(dataTye.name, name)
            else:
                res = "{}.write{}(_os, {})".format(dataTye.scope, dataTye.name, name)
        elif isinstance(dataTye, Enum):
            res = "_os.writeInt({})".format(name)

        return res

    def genJsonWriteExpr(self, dataType, varExpr, varName, currentScope):
        jsExpr = "js['{}']".format(varName)
        if isinstance(dataType, BasicType) or isinstance(dataType, Enum):
            self.write("{} = {}".format(jsExpr, varExpr))
        elif isinstance(dataType, Struct):
            self.write("{} = {}._toJson()".format(jsExpr, varExpr))
        elif isinstance(dataType, List) or isinstance(dataType, Dict):
            if dataType.scope == currentScope:
                self.write("{} = {}ToJson({})".format(jsExpr, dataType.name, varExpr))
            else:
                self.write("{} = {}.{}ToJson({})".format(jsExpr, dataType.scope, dataType.name, varExpr))

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
        self.write("def _read(self, _is):")
        self.indent = 2
        for field in structType.fields:
            fieldName = "self." + field.name
            expression = self.getPyReadExpression(field.type, fieldName, self.loader.scope)
            self.write(expression)
        self.writeEmptyLine()

        self.indent = 1
        self.write("def _write(self, _os):")
        self.indent = 2
        for field in structType.fields:
            fieldName = "self." + field.name
            expression = self.getPyWriteExpression(field.type, fieldName, self.loader.scope)
            self.write(expression)

        self.writeEmptyLine()
        self.indent = 1
        self.write("def _fromJson(self, js):")
        self.indent = 2
        for field in structType.fields:
            self.genJsonReadExpr(field.type, "self."+field.name, field.name, self.loader.scope)
        self.writeEmptyLine()

        self.indent = 1
        self.write("def _toJson(self):")
        self.indent = 2
        self.write("js = dict()")
        for field in structType.fields:
            self.genJsonWriteExpr(field.type, "self."+field.name, field.name, self.loader.scope)
        self.write("return js")
        self.writeEmptyLine()

        self.indent = 0
        self.write("MessageBlock.register({})".format(structType.name))
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

        self.write("def read{}(_is, valList):".format(capName))
        self.indent = 1
        self.write("dataSize = _is.readInt()")
        self.write("for _ in range(dataSize):")
        self.indent = 2
        initExpr = self.getTypePyInitExpression(listType.type, self.loader.scope)
        self.write("val = {}".format(initExpr))
        readExp = self.getPyReadExpression(listType.type, "val", self.loader.scope)
        self.write(readExp)
        self.write("valList.append(val)")

        self.indent = 0
        self.writeEmptyLine()

        self.write("def write{}(_os, valList):".format(capName))
        self.indent = 1
        self.write("dataSize = len(valList)")
        self.write("_os.writeInt(dataSize)")
        self.write("for val in valList:")
        self.indent = 2
        writeExp = self.getPyWriteExpression(listType.type, "val", self.loader.scope)
        self.write(writeExp)

        self.writeEmptyLine()
        self.indent = 0
        self.write("def {}FromJson(js):".format(capName))
        self.indent = 1
        if isinstance(listType.type, Struct):
            self.write("res = []")
            self.write("for js_c in js:")
            self.indent = 2
            initExpr = self.getTypePyInitExpression(listType.type, self.loader.scope)
            initExpr = "{} = {}".format("val", initExpr)
            self.write(initExpr)
            self.write("val._fromJson(js_c)")
            self.write("res.append(val)")
            self.indent = 1
            self.write("return res")
        elif isinstance(listType.type, List) or isinstance(listType.type, Dict):
            self.write("res = []")
            self.write("for js_c in js:")
            self.indent = 2
            if listType.type.scope == self.loader.scope:
                self.write("val = {}FromJson(js_c)".format(listType.type.name))
            else:
                self.write("val = {}.{}FromJson(js_c)".format(listType.type.scope, listType.type.name))
            self.write("res.append(val)")
            self.indent = 1
            self.write("return res")
        else:
            self.write("return js")
        self.writeEmptyLine()

        self.indent = 0
        self.write("def {}ToJson(valList):".format(capName))
        self.indent = 1
        if isinstance(listType.type, Struct):
            self.write("res = []")
            self.write("for val in valList:")
            self.indent = 2
            self.write("res.append(val._toJson())")
            self.indent = 1
            self.write("return res")
        elif isinstance(listType.type, List) or isinstance(listType.type, Dict):
            self.write("res = []")
            self.write("for val in valList:")
            self.indent = 2
            toExpr = ""
            if listType.type.scope == self.loader.scope:
                toExpr = "tmp = {}ToJson(val)".format(listType.type.name)
            else:
                toExpr = "tmp = {}.{}ToJson(val)".format(listType.type.scope, listType.type.name)
            self.write(toExpr)
            self.write("res.append(tmp)")
            self.indent = 1
            self.write("return res")
        else:
            self.write("return valList")

        self.indent = 0
        self.writeEmptyLine()

    def parseDict(self, dictType):
        self.indent = 0
        self.write("def read{}(_is, valDict):".format(dictType.name))
        self.indent = 1
        self.write("dataSize = _is.readInt()")
        self.write("for _ in range(dataSize):")
        self.indent = 2
        keyInitExpr = self.getTypePyInitExpression(dictType.keyType, self.loader.scope)
        keyInitExpr = "key_ = {}".format(keyInitExpr)
        valInitExpr = self.getTypePyInitExpression(dictType.valType, self.loader.scope)
        valInitExpr = "val_ = {}".format(valInitExpr)
        self.write(keyInitExpr)
        self.write(valInitExpr)
        keyReadExpr = self.getPyReadExpression(dictType.keyType, "key_", self.loader.scope)
        valReadExpr = self.getPyReadExpression(dictType.valType, "val_", self.loader.scope)
        self.write(keyReadExpr)
        self.write(valReadExpr)
        self.write("valDict[key_] = val_")

        self.indent = 0
        self.writeEmptyLine()

        self.write("def write{}(_os, valDict):".format(dictType.name))
        self.indent = 1
        self.write("dataSize = len(valDict)")
        self.write("_os.writeInt(dataSize)")
        self.write("for item in valDict.items():")
        self.indent = 2
        keyWriteExpr = self.getPyWriteExpression(dictType.keyType, "item[0]", self.loader.scope)
        valWriteExpr = self.getPyWriteExpression(dictType.valType, "item[1]", self.loader.scope)
        self.write(keyWriteExpr)
        self.write(valWriteExpr)

        self.writeEmptyLine()
        self.indent = 0
        self.write("def {}FromJson(js):".format(dictType.name))
        self.indent = 1
        if isinstance(dictType.valType, Struct):
            self.write("res = dict()")
            self.write("for key_ in js:")
            self.indent = 2
            initExpr = self.getTypePyInitExpression(dictType.valType, self.loader.scope)
            initExpr = "val = {}".format(initExpr)
            self.write(initExpr)
            self.write("val._fromJson(js[key_])")
            self.write("res[key_] = val")
            self.indent = 1
            self.write("return res")
        elif isinstance(dictType.valType, List) or isinstance(dictType.valType, Dict):
            self.write("res = dict()")
            self.write("for key_ in js:")
            self.indent = 2
            if dictType.valType.scope == self.loader.scope:
                self.write("res[key_] = {}FromJson(js[key_])".format(dictType.valType.name))
            else:
                self.write("res[key_] = {}.{}FromJson(js[key_])".format(dictType.valType.scope, dictType.valType.name))
            self.indent = 1
            self.write("return res")
        else:
            self.write("return js")

        self.writeEmptyLine()
        self.indent = 0
        self.write("def {}ToJson(valDict):".format(dictType.name))
        self.indent = 1
        if isinstance(dictType.valType, Struct):
            self.write("res = dict()")
            self.write("for key_ in valDict:")
            self.indent = 2
            self.write("res[key_] = valDict[key_]._toJson()")
            self.indent = 1
            self.write("return res")
        elif isinstance(dictType.valType, List) or isinstance(dictType.valType, Dict):
            self.write("res = dict()")
            self.write("for key_ in valDict:")
            self.indent = 2
            if dictType.valType.scope == self.loader.scope:
                self.write("res[key_] = {}ToJson(valDict[key_])".format(dictType.valType.name))
            else:
                self.write("res[key_] = {}.{}ToJson(valDict[key_])".format(dictType.valType.scope, dictType.valType.name))
            self.indent = 1
            self.write("return res")
        else:
            self.write("return valDict")

        self.indent = 0
        self.writeEmptyLine()

    def parseInterface(self, interfaceType):
        for method in interfaceType.methodList:
            self.parseRmiRequest(interfaceType, method)

        for method in interfaceType.methodList:
            self.parseRmiResponse(interfaceType, method)

        self.parseServant(interfaceType)
        self.parseProxy(interfaceType)

    def parseRmiRequest(self, interfaceType, method):
        self.indent = 0
        clsName = "{}_{}_Request".format(interfaceType.name, method.name.capitalize())
        self.write("class {}(RmiRequestBase):".format(clsName))
        self.indent = 1
        self.write("def __init__(self, connId, msgId, servant):")
        self.indent = 2
        self.write("super().__init__(connId, msgId, servant)")
        self.writeEmptyLine()
        self.indent = 1

        self.fout.write(self.getIndent(self.indent))
        self.fout.write("def response(self")
        for field in method.outfields:
            self.fout.write(", {}".format(field.name))
        self.fout.write("):\n")
        self.indent = 2
        self.write("_os = self._os")
        self.write("_os.writeInt(self.msgId)")
        for field in method.outfields:
            writeExpr = self.getPyWriteExpression(field.type, field.name, self.loader.scope)
            self.write(writeExpr)
        self.writeEmptyLine()
        self.write("self.sendout()")

        self.writeEmptyLine()

    def parseRmiResponse(self, interfaceType, method):
        self.indent = 0
        clsName = "{}_{}_Response".format(interfaceType.name, method.name.capitalize())
        self.write("class {}(RmiResponseBase):".format(clsName))
        self.indent = 1

        self.write("def __init__(self):")
        self.indent = 2
        self.write("super().__init__()")
        self.writeEmptyLine()
        self.indent = 1

        self.write("def _onResponse(self, _is):")
        self.indent = 2
        for field in method.outfields:
            initExpr = self.getTypePyInitExpression(field.type, self.loader.scope)
            initExpr = "{} = {}".format(field.name, initExpr)
            readExpr = self.getPyReadExpression(field.type, field.name, self.loader.scope)
            self.write(initExpr)
            self.write(readExpr)
        self.writeEmptyLine()

        self.fout.write(self.getIndent(self.indent))
        self.fout.write("self.onResponse(")
        isFirst = True
        for field in method.outfields:
            if not isFirst:
                self.fout.write(", ")
            else:
                isFirst = False
            self.fout.write(field.name)
        self.fout.write(")\n")
        self.writeEmptyLine()

        self.indent = 1
        self.write("@abc.abstractmethod")
        self.fout.write(self.getIndent(self.indent))
        self.fout.write("def onResponse(self")
        for field in method.outfields:
            self.fout.write(", {}".format(field.name))
        self.fout.write("):\n")
        self.indent = 2
        self.write("pass")

        self.writeEmptyLine()
        self.indent = 1
        self.write("@abc.abstractmethod")
        self.write("def onError(self, what, code):")
        self.indent = 2
        self.write("pass")

        self.writeEmptyLine()
        self.indent = 1
        self.write("@abc.abstractmethod")
        self.write("def onTimeout(self):")
        self.indent = 2
        self.write("pass")
        self.writeEmptyLine()
        self.writeEmptyLine()

    def parseServant(self, interfaceType):
        clsName = "{}Servant".format(interfaceType.name)
        self.indent = 0

        self.write("class {}(RmiServant):".format(clsName))
        self.indent = 1
        self.write("def __init__(self, name):")
        self.indent = 2
        self.write("super().__init__(name)")
        for method in interfaceType.methodList:
            self.write("self.methodMap['{0}'] = self._{0}".format(method.name))
        self.writeEmptyLine()

        self.indent = 1
        for method in interfaceType.methodList:
            self.indent = 1
            self.write("def _{}(self, _connId, _msgId, _is):".format(method.name))
            self.indent = 2
            for field in method.infields:
                initExpr = self.getTypePyInitExpression(field.type, self.loader.scope)
                initExpr = "{} = {}".format(field.name, initExpr)
                readExpr = self.getPyReadExpression(field.type, field.name, self.loader.scope)
                self.write(initExpr)
                self.write(readExpr)
            clsName = "{}_{}_Request".format(interfaceType.name, method.name.capitalize())
            self.write("_request = {}(_connId, _msgId, self)".format(clsName))
            self.fout.write(self.getIndent(self.indent))
            self.fout.write("self.{}(".format(method.name))
            for field in method.infields:
                self.fout.write("{}, ".format(field.name))
            self.fout.write("_request)\n")
            self.indent = 1
            self.writeEmptyLine()
            self.write("@abc.abstractmethod")
            self.fout.write(self.getIndent(self.indent))
            self.fout.write("def {}(self".format(method.name))
            for field in method.infields:
                self.fout.write(", {}".format(field.name))
            self.fout.write(", _request):\n")
            self.indent = 2
            self.write("pass")
            self.writeEmptyLine()

    def parseProxy(self, interfaceType):
        clsName = "{}Proxy".format(interfaceType.name)
        self.indent = 0
        self.write("class {}(RmiProxy):".format(clsName))

        self.indent = 1
        self.write("def __init__(self, name):")
        self.indent = 2
        self.write("super().__init__(name)")
        self.writeEmptyLine()

        for method in interfaceType.methodList:
            self.indent = 1
            self.fout.write(self.getIndent(self.indent))
            self.fout.write("def {}(self, _response".format(method.name))
            for field in method.infields:
                self.fout.write(", {}".format(field.name))
            self.fout.write("):\n")
            self.indent = 2
            self.write("_os = Serializer()")
            self.write("_os.startToWrite()")
            self.write("_os.writeByte(RmiDataType.RmiCall)")
            self.write("_os.writeString(self.name)")
            self.write("_os.writeString('{}')".format(method.name))
            self.write("_msgId = self.getMsgId()")
            self.write("_os.writeInt(_msgId)")
            self.write("_response._setMsgId(_msgId)")
            for field in method.infields:
                writeExpr = self.getPyWriteExpression(field.type, field.name, self.loader.scope)
                self.write(writeExpr)
            self.write("self.invoke(_os, _response)")
            self.writeEmptyLine()
        self.writeEmptyLine()

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
