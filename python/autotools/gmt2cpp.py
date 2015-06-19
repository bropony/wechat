"""
* @name gmt2cpp.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/16 15:01
*
* @desc gmt2cpp.py
"""

import sys
import os.path
import re
import datetime
from optparse import OptionParser

from gmtloader.loader import *
from gmtloader.structmanager import StructManager

class Gmt2Cpp:
    @staticmethod
    def raiseExcept(what):
        raise Exception(what)

    def __init__(self, structManager, loader):
        self.structManager = structManager
        self.loader = loader
        self.cppIndent = 0
        self.hppIndent = 0
        self.fhpp = None
        self.fcpp = None
        self.cppName = ""
        self.hppName = ""
        self.scopes = []
        self.cppScope = ""
        self.macro = ""

    @staticmethod
    def _getIndent(indent):
        if not indent:
            return ""

        return "    " * indent

    def _getCppIndent(self):
        return self._getIndent(self.cppIndent)

    def _getHppIndent(self):
        return self._getIndent(self.hppIndent)

    def _write(self, fout, indent, line=None, endl=True):
        if line:
            res = "{}{}".format(indent, line)
            fout.write(res)

        if endl:
            fout.write("\n")

    def writeHpp(self, line=None, endl=True):
        self._write(self.fhpp, self._getHppIndent(), line, endl)

    def writeCpp(self, line=None, endl=True):
        self._write(self.fcpp, self._getCppIndent(), line, endl)

    def openFiles(self, rootDir):
        if not os.path.exists(rootDir):
            self.raiseExcept("outdir {} does not exist".format(rootDir))

        packages = re.split(r'\.', self.loader.scope)
        self.scopes = packages
        self.cppScope = "::".join(packages)

        subDir = "/".join(packages[:-1])
        absDir = os.path.join(rootDir, subDir)
        if not os.path.exists(absDir):
            os.makedirs(absDir)

        self.cppName = packages[-1] + ".cpp"
        self.hppName = packages[-1] + ".h"

        self.fcpp = open(os.path.join(absDir, self.cppName), 'w')
        self.fhpp = open(os.path.join(absDir, self.hppName), 'w')

        self.macro = "__{}_H__".format("_".join(self.scopes)).upper()

    def closeFiles(self):
        self.fcpp.close()
        self.fhpp.close()

    def generate(self):
        print("Generation C++ code for {}".format(self.loader.filepath))
        outRootDir = self.structManager.outRootDir
        self.openFiles(outRootDir)

        self.writeComments()
        self.writeIncludes()
        self.begin()

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

        self.end()

        self.closeFiles()

    def writeComments(self):
        self.writeHpp("/*")
        self.writeHpp("* @filename {}".format(self.hppName))
        self.writeHpp("*")
        self.writeHpp("* @author ahda86@gmail.com")
        self.writeHpp("*")
        self.writeHpp("* @brief This files is Auto-Generated. Please DON'T modify it EVEN if")
        self.writeHpp("*        you know what you are doing.")
        self.writeHpp("*/")
        self.writeHpp()

        self.writeCpp("/*")
        self.writeCpp("* @filename {}".format(self.cppName))
        self.writeCpp("*")
        self.writeCpp("* @author ahda86@gmail.com")
        self.writeCpp("*")
        self.writeCpp("* @brief This files is Auto-Generated. Please DON'T modify it EVEN if")
        self.writeCpp("*        you know what you are doing.")
        self.writeCpp("*/")
        self.writeCpp()

    def writeIncludes(self):
        self.writeHpp("#ifndef {}".format(self.macro))
        self.writeHpp("#define {}".format(self.macro))
        self.writeHpp()

        self.writeHpp("#include <map>")
        self.writeHpp("#include <vector>")
        self.writeHpp("#include <gamit/util/autorun.h>")
        self.writeHpp("#include <gamit/util/sharedptr.h>")
        self.writeHpp("#include <gamit/serialize/serializer.h>")
        self.writeHpp("#include <gamit/rmi/RmiCore.h>")
        self.writeHpp("#include <gamit/message/Message.h>")

        for inc in self.loader.includes:
            fields = re.split(r'\.', inc)
            self.writeHpp("#include <{}.h>".format("/".join(fields)))
        self.writeHpp()

        self.writeCpp("#include <{}.h>".format("/".join(self.scopes)))
        self.writeCpp()

    def begin(self):
        for scope in self.scopes:
            self.writeHpp("namespace {}{}".format(scope, "{"))
            self.hppIndent += 1
        self.writeHpp()

    def end(self):
        for scope in self.scopes:
            self.hppIndent -= 1
            self.writeHpp("}")

        self.writeHpp()
        self.writeHpp("#endif //{}".format(self.macro))

    def getCppType(self, dataType):
        if isinstance(dataType, BasicType):
            if dataType.name == "byte":
                return "byte_t"
            elif dataType.name == "long":
                return "long64_t"
            elif dataType.name == "string":
                return "std::string"
            elif dataType.name == "binary":
                return "std::string"
            elif dataType.name == "date":
                return "gamit::CDateTime"
            else:
                return dataType.name
        else:
            return dataType.fullname.replace(".", "::")

    def getRefForm(self, dataType):
        if isinstance(dataType, BasicType):
            if dataType.name == "string" or dataType.name == "binary":
                return "const std::string &"
            elif dataType.name == "date":
                return "const gamit::CDateTime &"
            else:
                return self.getCppType(dataType)
        elif isinstance(dataType, Enum):
            return dataType.fullname.replace(".", "::")
        else:
            return "const " + dataType.fullname.replace(".", "::") + " &"

    def getReadExpr(self, varName, dataType):
        res = "readExpr:Oops"
        if isinstance(dataType, BasicType):
            res = "__is.read({})".format(varName)
        elif isinstance(dataType, Struct):
            res = "{}.__read(__is)".format(varName)
        elif isinstance(dataType, Dict) or isinstance(dataType, List):
            scope = dataType.scope.replace(".", "::")
            res = "{0}::__read(__is, {1}, {0}::__{2}_U__())".format(scope, varName, dataType.name)
        elif isinstance(dataType, Enum):
            scope = dataType.scope.replace(".", "::")
            res = "{}::read(__is, {})".format(scope, varName)

        return res

    def getWriteExpr(self, varName, dataType):
        res = "writeExpr:Oops"
        if isinstance(dataType, BasicType):
            res = "__os.write({})".format(varName)
        elif isinstance(dataType, Struct):
            res = "{}.__write(__os)".format(varName)
        elif isinstance(dataType, List) or isinstance(dataType, Dict):
            scope = dataType.scope.replace(".", "::")
            res = "{0}::__write(__os, {1}, {0}::__{2}_U__())".format(scope, varName, dataType.name)
        elif isinstance(dataType, Enum):
            scope = dataType.scope.replace(".", "::")
            res = "{}::write(__os, {})".format(scope, varName)

        return  res

    def parseStruct(self, dataType):
        structName = dataType.name
        classScope = "{}::{}".format(self.cppScope, structName)
        self.writeHpp("//{}".format(structName))
        self.writeHpp("class {};".format(structName))
        self.writeHpp("typedef std::CSharedPtr<{0}> {0}Ptr;".format(structName))
        self.writeHpp("class {}: public gamit::MessageBase".format(structName))
        self.writeHpp("{") # begin of class
        self.writeHpp("public:")
        self.hppIndent += 1

        self.writeCpp("// implementation of class {}".format(structName))
        self.writeCpp("gamit::CAutoRun regist{1}({0}::{1}::regist);".format(self.cppScope, structName))
        self.writeCpp("std::string {}::_msgName(\"{}\");".format(classScope, structName))
        self.writeCpp()

        for field in dataType.fields:
            self.writeHpp("{} {};".format(self.getCppType(field.type), field.name))

        # regist
        self.writeHpp()
        self.writeHpp("static void regist();")
        self.writeHpp("static const {}Ptr create();".format(structName))
        self.writeHpp()

        # regist func
        self.writeCpp("void {}::regist()".format(classScope))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp('gamit::MessageBlock::registCreateFunc("{0}", {0}::create);'.format(structName))
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

        # create func
        self.writeCpp("const {}::{}Ptr {}::create()".format(self.cppScope, structName, classScope))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("return (new {}());".format(structName))
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

        # read and write
        self.writeHpp("virtual void __read(gamit::CSerializer & __is);")
        self.writeHpp("virtual void __write(gamit::CSerializer & __os) const;")
        self.writeHpp("virtual const std::string & __name() const;")
        self.writeHpp()

        # __read
        self.writeCpp("void {}::__read(gamit::CSerializer & __is)".format(classScope))
        self.writeCpp("{")
        self.cppIndent += 1
        for field in dataType.fields:
            readExpr = self.getReadExpr(field.name, field.type)
            self.writeCpp("{};".format(readExpr))
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()  # end of __read

        # __write
        self.writeCpp("void {}::__write(gamit::CSerializer & __os) const".format(classScope))
        self.writeCpp("{")
        self.cppIndent += 1
        for field in dataType.fields:
            writeExpr = self.getWriteExpr(field.name, field.type)
            self.writeCpp("{};".format(writeExpr))
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()  # end of __write

        # __name
        self.writeCpp("const std::string & {}::__name() const".format(classScope))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("return _msgName;")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

        # private
        self.hppIndent -= 1
        self.writeHpp("private:")
        self.hppIndent += 1
        self.writeHpp("static std::string _msgName;")

        self.hppIndent -= 1 # end of class
        self.writeHpp("{}; // class {}".format("}", structName))
        self.writeHpp()

    def parseEnum(self, dataType):
        enumName = dataType.name
        enumFullName = dataType.fullname.replace(".", "::")
        self.writeHpp("// enum class {}".format(enumName))
        self.writeHpp("enum class {}".format(enumName))
        self.writeHpp("{")
        self.hppIndent += 1
        for pair in dataType.pairs:
            self.writeHpp("{} = {},".format(*pair))
        self.hppIndent -= 1
        self.writeHpp("};")
        self.writeHpp("void read(gamit::CSerializer & __is, {} & __val);".format(enumName))
        self.writeHpp("void write(gamit::CSerializer & __os, {} __val);".format(enumName))
        self.writeHpp()

        self.writeCpp("void {}::read(gamit::CSerializer & __is, {} &__val)".format(self.cppScope, enumFullName))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("int __i = 0;")
        self.writeCpp("__is.read(__i);")
        self.writeCpp("__val = {}(__i);".format(enumFullName))
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

        self.writeCpp("void {}::write(gamit::CSerializer & __os, {} __val)".format(self.cppScope, enumFullName))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("__os.write(int(__val));")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

    def parseList(self, dataType):
        listName = dataType.name
        listFullName = dataType.fullname.replace(".", "::")
        typeName = self.getCppType(dataType.type)
        uniqueClassName = "__{}_U__".format(listName)

        self.writeHpp("// {}".format(listName))
        self.writeHpp("typedef std::vector< {} > {};".format(self.getCppType(dataType.type), listName))
        self.writeHpp("class {}{};".format(uniqueClassName, "{}"))
        self.writeHpp("void __read(gamit::CSerializer & __is, {} & __valList, {});".format(listName, uniqueClassName))
        self.writeHpp("void __write(gamit::CSerializer & __os, const {} &__valList, {});".format(listName, uniqueClassName))
        self.writeHpp()

        self.writeCpp(
            "void {}::__read(gamit::CSerializer & __is, {}::{} & __valList, {})".format(
                self.cppScope, self.cppScope, listName, uniqueClassName))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("int __size = 0;")
        self.writeCpp("__is.read(__size);")
        self.writeCpp("for (int i = 0; i < __size; ++i)")
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("{} __val;".format(typeName))
        readExpr = self.getReadExpr("__val", dataType.type)
        self.writeCpp("{};".format(readExpr))
        self.writeCpp("__valList.push_back(__val);")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

        self.writeCpp(
            "void {}::__write(gamit::CSerializer & __os, const {}::{} & __valList, {})".format(
                self.cppScope, self.cppScope, listName, uniqueClassName))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("__os.writeSize(__valList.size());")
        self.writeCpp("for (auto __val: __valList)")
        self.writeCpp("{")
        self.cppIndent += 1
        writeExpr = self.getWriteExpr("__val", dataType.type)
        self.writeCpp(writeExpr + ";")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

    def parseDict(self, dataType):
        dictName = dataType.name
        dictFullName = dataType.fullname.replace(".", "::")
        keyName = self.getCppType(dataType.keyType)
        valName = self.getCppType(dataType.valType)
        uniqueClassName = "__{}_U__".format(dictName)

        self.writeHpp("// {}".format(dictName))
        self.writeHpp("typedef std::map< {}, {} > {};".format(keyName, valName, dictName))
        self.writeHpp("class {}{};".format(uniqueClassName, "{}"))

        self.writeHpp("void __read(gamit::CSerializer & __is, {} & __valDict, {});".format(dictName, uniqueClassName))
        self.writeHpp("void __write(gamit::CSerializer & __os, const {} &__valDict, {});".format(dictName, uniqueClassName))
        self.writeHpp()

        self.writeCpp(
            "void {}::__read(gamit::CSerializer & __is, {} & __valDict, {})".format(
                self.cppScope, dictFullName, uniqueClassName))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("int __size = 0;")
        self.writeCpp("__is.read(__size);")
        self.writeCpp("for (int i = 0; i < __size; ++i)")
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("{} __key;".format(keyName))
        self.writeCpp("{} __val;".format(valName))
        readKeyExpr = self.getReadExpr("__key", dataType.keyType)
        readValExpr = self.getReadExpr("__val", dataType.valType)
        self.writeCpp(readKeyExpr + ";")
        self.writeCpp(readValExpr + ";")
        self.writeCpp("__valDict.insert({__key, __val});")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

        self.writeCpp(
            "void {}::__write(gamit::CSerializer & __os, const {} & __valDict, {})".format(
                self.cppScope, dictFullName, uniqueClassName))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("__os.writeSize(__valDict.size());")
        self.writeCpp("for (auto __pair: __valDict)")
        self.writeCpp("{")
        self.cppIndent += 1
        writeKeyExpr = self.getWriteExpr("__pair.first", dataType.keyType)
        writeValExpr = self.getWriteExpr("__pair.second", dataType.valType)
        self.writeCpp(writeKeyExpr + ";")
        self.writeCpp(writeValExpr + ";")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

    def parseInterface(self, dataType):
        for method in dataType.methodList:
            self.parseResponse(dataType, method)

        self.parseProxy(dataType)

    def parseResponse(self, interfaceType, method):
        className = "{}_{}_Response".format(interfaceType.name, method.name)
        classFullName = "{}::{}".format(self.cppScope, className)
        self.writeHpp("// {}".format(className))
        self.writeHpp("class {}: public gamit::CRmiResponseBase".format(className))
        self.writeHpp("{")
        self.hppIndent += 1
        self.writeHpp("virtual void __onResponse(gamit::CSerializer & __is);")
        self.writeHpp("virtual void __onError(gamit::CSerializer & __is);")
        self.writeHpp("virtual void __onTimeout();")
        self.writeHpp()
        self.fhpp.write(self._getHppIndent())
        self.fhpp.write("virtual void onResponse(")
        isFirst = True
        for field in method.outfields:
            if isFirst:
                isFirst = False
            else:
                self.fhpp.write(",")

            ref = self.getRefForm(field.type)
            self.fhpp.write("{} {}".format(ref, field.name))

        self.fhpp.write(") = 0;\n")
        self.writeHpp("virtual void onError(const std::string & what, int code) = 0;")
        self.writeHpp("virtual void onTimeout() = 0;")
        self.hppIndent -= 1
        self.writeHpp("{}; // class {}".format("}", className))
        self.writeHpp("typedef std::CSharedPtr<{0}> {0}Ptr;".format(className))
        self.writeHpp()

        self.writeCpp("void {}::__onResponse(gamit::CSerializer & __is)".format(classFullName))
        self.writeCpp("{")
        self.cppIndent += 1
        for field in method.outfields:
            self.writeCpp("{} {};".format(self.getCppType(field.type), field.name))
            self.writeCpp("{};".format(self.getReadExpr(field.name, field.type)))
        self.writeCpp("onResponse(", False)
        isFirst = True
        for field in method.outfields:
            if isFirst:
                isFirst = False
            else:
                self.fcpp.write(",")
            self.fcpp.write(field.name)
        self.fcpp.write(");\n")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

        self.writeCpp("void {}::__onError(gamit::CSerializer & __is)".format(classFullName))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("std::string __what;")
        self.writeCpp("__is.read(__what);")
        self.writeCpp("int __code;")
        self.writeCpp("__is.read(__code);")
        self.writeCpp("onError(__what, __code);")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

        self.writeCpp("void {}::__onTimeout()".format(classFullName))
        self.writeCpp("{")
        self.cppIndent += 1
        self.writeCpp("onTimeout();")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

    def parseProxy(self, interfaceType):
        className = interfaceType.name
        classFullName = interfaceType.fullname.replace(".", "::")

        self.writeCpp('std::string {}::__proxyName("{}");'.format(classFullName, className))
        self.writeCpp()

        self.writeHpp("// {}".format(className))
        self.writeHpp("class {}: public gamit::CRmiProxyBase".format(className))
        self.writeHpp("{")
        self.writeHpp("public:")
        self.hppIndent += 1

        for method in interfaceType.methodList:
            self.parseCallout(className, classFullName, method)

        self.writeHpp()
        self.hppIndent -= 1
        self.writeHpp("private:")
        self.hppIndent += 1
        self.writeHpp("static std::string __proxyName;")

        self.hppIndent -= 1
        self.writeHpp("{}; // class {}".format("}", className))
        self.writeHpp("typedef std::CSharedPtr<{}> {}Ptr;".format(className, className))
        self.writeHpp()

    def parseCallout(self, className, classFullName, method):
        responseName = "{}_{}_ResponsePtr".format(className, method.name)
        self.writeHpp("void {}(const {} &".format(method.name, responseName), False)
        for field in method.infields:
            self.fhpp.write(", {} {}".format(self.getRefForm(field.type), field.name))
        self.fhpp.write(");\n")

        self.writeCpp("void {}::{}(const {} & __cb".format(classFullName, method.name, responseName), False)
        for field in method.infields:
            self.fcpp.write(", {} {}".format(self.getRefForm(field.type), field.name))
        self.fcpp.write(")\n")
        self.writeCpp("{")
        self.cppIndent += 1

        self.writeCpp('static std::string __methodName = "{}";'.format(method.name))
        self.writeCpp()
        self.writeCpp("gamit::CSerializer __os;")
        self.writeCpp("__os.startToWrite();")
        self.writeCpp()
        self.writeCpp("__os.write(int(gamit::ERmiType::RmiCall));")
        self.writeCpp('__os.write(__proxyName);')
        self.writeCpp("__os.write(__methodName);")
        self.writeCpp()
        self.writeCpp("int __msgId = __getMsgId();")
        self.writeCpp("__os.write(__msgId);")
        self.writeCpp("__cb->setMsgId(__msgId);")
        self.writeCpp()
        for field in method.infields:
            writeExpr = self.getWriteExpr(field.name, field.type)
            self.writeCpp(writeExpr + ";")

        if method.infields:
            self.writeCpp()

        self.writeCpp("invoke(__os, __cb);")
        self.cppIndent -= 1
        self.writeCpp("}")
        self.writeCpp()

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
        gmt = Gmt2Cpp(structManager, loader)
        gmt.generate()

if __name__ == "__main__":
    main()
