__author__ = 'mahanzhou'


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

class Gmt2Objc:
    @staticmethod
    def raiseExcept(what):
        raise Exception(what)

    def __init__(self, structManager, loader):
        self.structManager = structManager
        self.loader = loader
        self.mmIndent = 0
        self.hhIndent = 0
        self.fmm = None
        self.fhh = None
        self.mmName = ""
        self.hhName = ""

    @staticmethod
    def _getIndent(indent):
        if not indent:
            return ""

        return "    " * indent

    def _getMmIndent(self):
        return self._getIndent(self.mmIndent)

    def _getHhIndent(self):
        return self._getIndent(self.hhIndent)

    def _write(self, fout, indent, line=None, endl=True):
        if line:
            res = "{}{}".format(indent, line)
            fout.write(res)

        if endl:
            fout.write("\n")

    def writeMm(self, line=None, endl=True):
        self._write(self.fmm, self._getMmIndent(), line, endl)

    def writeHh(self, line=None, endl=True):
        self._write(self.fhh, self._getHhIndent(), line, endl)

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

        self.mmName = packages[-1] + ".m"
        self.hhName = packages[-1] + ".h"

        self.fmm = open(os.path.join(absDir, self.mmName), 'w')
        self.fhh = open(os.path.join(absDir, self.hhName), 'w')

    def closeFiles(self):
        self.fhh.close()
        self.fmm.close()

    def generate(self):
        print("Generation objective-C code for {}".format(self.loader.filepath))
        outRootDir = self.structManager.outRootDir
        self.openFiles(outRootDir)

        self.writeComments()
        self.writeImports()
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
        self.writeHh("/*")
        self.writeHh("* @filename {}".format(self.hhName))
        self.writeHh("*")
        self.writeHh("* @author ahda86@gmail.com")
        self.writeHh("*")
        self.writeHh("* @brief This files is Auto-Generated. Please DON'T modify it EVEN if")
        self.writeHh("*        you know what you are doing.")
        self.writeHh("*/")
        self.writeHh()

        self.writeMm("/*")
        self.writeMm("* @filename {}".format(self.cppName))
        self.writeMm("*")
        self.writeMm("* @author ahda86@gmail.com")
        self.writeMm("*")
        self.writeMm("* @brief This files is Auto-Generated. Please DON'T modify it EVEN if")
        self.writeMm("*        you know what you are doing.")
        self.writeMm("*/")
        self.writeMm()

    def writeImports(self):
        self.writeHh("#import <Foundation/Foundation.h>")

        for inc in self.loader.includes:
            fields = re.split(r'\.', inc)
            self.writeHh("#import <{}.h>".format("/".join(fields)))
        self.writeHpp()

        self.writeMm("#import <{}.h>".format("/".join(self.scopes)))
        self.writeMm()

    def begin(self):
        pass

    def end(self):
        pass

    def getObjcClassName(self, name):
        return "GY" + name

    def getOjbcType(self, dataType):
        if isinstance(dataType, BasicType):
            if dataType.name == 'bool':
                return "BOOL"
            if dataType.name == "string":
                return "NSString"
            if dataType.name == "date":
                return "NSDate"
            if dataType.name == "binary":
                return "NSString"
            return "NSNumber"

        if isinstance(dataType, Enum):
            pass

    def parseStruct(self, dataType):
        className = self.getObjcClassName(dataType.name)

        self.writeHh("@interface {}".format(className))
        for field in dataType.fields:
            pass

        self.writeHh("@end")

    def parseEnum(self, dataType):
        pass

    def parseList(self, dataType):
        pass

    def parseDict(self, dataType):
        pass

    def parseInterface(self, dataType):
        for method in dataType.methodList:
            self.parseResponse(dataType, method)

        self.parseProxy(dataType)

    def parseResponse(self, interfaceType, method):
        pass

    def parseProxy(self, interfaceType):
        pass


def main():
    parser = OptionParser()
    parser.add_option("-n", "--namespace", help="root python module name",
                      dest="scope")
    parser.add_option("-g", "--gmt-dir", help="root directory of gmt files",
                      dest="inRootDir")
    parser.add_option("-o", "--out-dir", help="root directory of generated objective-C files",
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
        gmt = Gmt2Objc(structManager, loader)
        gmt.generate()

if __name__ == "__main__":
    main()
