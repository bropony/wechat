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
        self.writeHpp("#include <gamit/util/sharedptr.h>")
        self.writeHpp("#include <gamit/serialize/serializer.h>")
        self.writeHpp("#include <gamit/rmi/RmiCore.h>")
        self.writeHpp("#include <gamit/message/Message.h>")

        for inc in self.loader.includes:
            fields = re.split(r'\.', inc)
            self.writeHpp("#include <{}.h>".format("/".join(fields)))
        self.writeHpp()

        self.writeCpp("#include <.h>".format("/".join(self.scopes)))
        self.writeCpp()

    def begin(self):
        for scope in self.scopes:
            self.writeHpp("namespace {}{}".format(scope, "{"))
            self.hppIndent += 1

    def end(self):
        self.writeHpp()
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
                return "gamit::CDatetime"
            else:
                return dataType.name
        else:
            return dataType.fullname.replace(".", "::")

    def parseStruct(self, dataType):
        structName = dataType.name
        self.writeHpp("class {}: public gamit::MessageBase".format(structName))
        self.writeHpp("{") # begin of class
        self.writeHpp("public:")
        self.hppIndent += 1

        for field in dataType.fields:
            self.writeHpp("{} {};".format(self.getCppType(field.type), field.name))

        self.hppIndent -= 1 # end of class
        self.writeHpp("};")
        self.writeHpp()

    def parseList(self, dataType):
        pass

    def parseDict(self, dataType):
        pass

    def parseInterface(self, dataType):
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
        gmt = Gmt2Cpp(structManager, loader)
        gmt.generate()

if __name__ == "__main__":
    main()
