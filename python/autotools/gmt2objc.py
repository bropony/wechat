__author__ = 'mahanzhou'


"""
* @name gmt2objc.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/16 15:01
*
* @desc gmt2objc.py
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
        self.writeMm("* @filename {}".format(self.mmName))
        self.writeMm("*")
        self.writeMm("* @author ahda86@gmail.com")
        self.writeMm("*")
        self.writeMm("* @brief This files is Auto-Generated. Please DON'T modify it EVEN if")
        self.writeMm("*        you know what you are doing.")
        self.writeMm("*/")
        self.writeMm()

    def writeImports(self):
        self.writeHh("#import \"gamit.h\"")

        for inc in self.loader.includes:
            fields = re.split(r'\.', inc)
            self.writeHh("#import \"{}.h\"".format(fields[-1]))
        self.writeHh()

        self.writeMm("#import \"{}.h\"".format(self.scopes[-1]))
        self.writeMm()

    def begin(self):
        pass

    def end(self):
        pass

    def getObjcClassName(self, name):
        return name

    def getPropertyDeclare(self, field):
        res = "@property"
        if isinstance(field.type, BasicType):
            if field.type.name in ("string", "date", "binary"):
                res += " (copy, nonatomic)"
        elif not isinstance(field.type, Enum):
            res += " (copy, nonatomic)"

        res += " {} {}".format(self.getObjcRef(field.type), field.name)
        return res

    def getObjcType(self, dataType):
        if isinstance(dataType, BasicType):
            if dataType.name == 'bool':
                return "GYBool"
            if dataType.name == "string":
                return "NSString"
            if dataType.name == "date":
                return "NSDate"
            if dataType.name == "binary":
                return "NSData"

            return "GY" + dataType.name.capitalize()

        if isinstance(dataType, Enum):
            return "enum " + self.getObjcClassName(dataType.name)

        return dataType.name

    def getObjcRef(self, dataType):
        if isinstance(dataType, BasicType):
            if dataType.name == 'bool':
                return "GYBool"
            if dataType.name == "string":
                return "NSString *"
            if dataType.name == "date":
                return "NSDate *"
            if dataType.name == "binary":
                return "NSData *"

            return "GY" + dataType.name.capitalize()

        if isinstance(dataType, Enum):
            return "enum " + self.getObjcClassName(dataType.name)

        return dataType.name + " *"

    def getInitValue(self, dataType):
        if dataType.name == "bool":
            return "NO"
        if dataType.name in ("byte", "short", "int", "long"):
            return "0"
        if dataType.name in ("float", "double"):
            return "0.0"
        if dataType.name == "enum":
            return dataType.name + dataType.pairs[0][0]
        if dataType.name == "string":
            return '@""'
        if dataType.name == "date":
            return "[NSDate date]"

        if isinstance(dataType, Enum):
            return "{}{}".format(dataType.name, dataType.pairs[0][0])

        return "[[{} alloc] init]".format(dataType.name)

    def getReadExpr(self, dataType, varName):
        if isinstance(dataType, BasicType):
            return "{} = [__is read{}];".format(varName, dataType.name.capitalize())

        if isinstance(dataType, Enum):
            return "{} = (enum {})[__is readInt];".format(varName, dataType.name)

        return "[{} __read: __is];".format(varName)

    def getWriteExpr(self, dataType, varName):
        if isinstance(dataType, BasicType):
            return "[__os write{}: {}];".format(dataType.name.capitalize(), varName)

        if isinstance(dataType, Enum):
            return "[__os writeInt: {}];".format(varName)

        return "[{} __write: __os];".format(varName)

    def getCopyExpr(self, dataType, varName):
        if isinstance(dataType, BasicType):
            if dataType.name in ("string", "date", "binary"):
                return "[{} copy]".format(varName)
            return varName
        if isinstance(dataType, Enum):
            return varName

        return "[{} copy]".format(varName)

    def cap(self, name):
        if not name:
            return name
        return name[0].capitalize() + name[1:]

    def parseStruct(self, dataType):
        # className = self.getObjcClassName(dataType.name)
        className = dataType.name

        self.writeHh("// class {}".format(className))
        self.writeHh("@interface {}: NSObject <GYMessageBaseProtocol>".format(className))
        self.writeHh()
        self.writeMm("@implementation {}".format(className))
        self.writeMm()
        for field in dataType.fields:
            self.writeHh(self.getPropertyDeclare(field) + ";")
            self.writeMm("@synthesize {};".format(field.name))
        self.writeHh()
        self.writeMm()

        self.writeHh("- (id) init;")
        self.writeHh("- (void) __read: (GYSerializer *) __is;")
        self.writeHh("- (void) __write: (GYSerializer *) __os;")
        self.writeHh("- (id) copyWithZone: (NSZone *) zone;")
        self.writeHh("@end")
        self.writeHh()
        self.writeHh()

        # - (id) init
        self.writeMm("- (id) init")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("self = [super init];")
        self.writeMm("if (!self) return self;")
        self.writeMm()
        for field in dataType.fields:
            self.writeMm("{} = {};".format(field.name, self.getInitValue(field.type)))

        self.writeMm()
        self.writeMm("return self;")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (void) __read
        self.writeMm("- (void) __read: (GYSerializer *) __is")
        self.writeMm("{")
        self.mmIndent += 1
        for field in dataType.fields:
            self.writeMm(self.getReadExpr(field.type, field.name))
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (void) __write
        self.writeMm("- (void) __write: (GYSerializer *) __os")
        self.writeMm("{")
        self.mmIndent += 1
        for field in dataType.fields:
            self.writeMm(self.getWriteExpr(field.type, field.name))

        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (id) copyWithZone
        self.writeMm("- (id) copyWithZone: (NSZone *) zone")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("id __newObj = [[[self class] allocWithZone: zone] init];")
        self.writeMm()
        for field in dataType.fields:
            self.writeMm("[__newObj set{}: {}];".format(self.cap(field.name), self.getCopyExpr(field.type, "self." + field.name)))
        self.writeMm()
        self.writeMm("return __newObj;")
        self.mmIndent -= 1
        self.writeMm("}")

        self.writeMm("@end")
        self.writeMm()
        self.writeMm()

    def parseEnum(self, dataType):
        enumName = dataType.name

        self.writeHh("enum {}: GYInt".format(enumName))
        self.writeHh("{")
        self.hhIndent += 1

        for pair in dataType.pairs:
            self.writeHh("{}{} = {},".format(enumName, pair[0], pair[1]))

        self.hhIndent -= 1
        self.writeHh("};")
        self.writeHh()

    def parseList(self, dataType):
        listName = dataType.name

        self.writeHh("// " + listName)
        self.writeHh("@interface {}: NSObject <GYMessageBaseProtocol>".format(listName))
        self.writeHh("@property (copy, nonatomic) NSMutableArray * data;")
        self.writeHh()
        self.writeHh("- (id) init;")
        self.writeHh("- (void) __read: (GYSerializer *) __is;")
        self.writeHh("- (void) __write: (GYSerializer *) __os;")
        self.writeHh("- (id) copyWithZone: (NSZone *) zone;")
        self.writeHh("@end")
        self.writeHh()
        self.writeHh()

        self.writeMm("@implementation {}".format(listName))

        # - (id) init
        self.writeMm("- (id) init")
        self.writeMm("{")
        self.mmIndent += 1

        self.writeMm("self = [super init];")
        self.writeMm("if (!self) return self;")
        self.writeMm()
        self.writeMm("_data = [[NSMutableArray alloc] init];")
        self.writeMm("return self;")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (void) __read
        self.writeMm("- (void) __read: (GYSerializer *) __is")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("GYInt dataSize = [__is readInt];")
        self.writeMm("for (GYInt i = 0; i < dataSize; ++i)")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("{} {} = {};".format(self.getObjcRef(dataType.type), "__tmpObj", self.getInitValue(dataType.type)))
        self.writeMm(self.getReadExpr(dataType.type, "__tmpObj"))
        self.writeMm("[_data addObject: {}];".format(self._basicToObjectExpr(dataType.type, "__tmpObj")))
        self.mmIndent -= 1
        self.writeMm("}")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (void) __write
        self.writeMm("- (void) __write: (GYSerializer *) __os")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("GYInt dataSize = (GYInt)[_data count];")
        self.writeMm("[__os writeInt: dataSize];")
        self.writeMm("for (id obj in _data)")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm(self.getWriteExpr(dataType.type, self._objectToBasicExpr(dataType.type, "obj")))
        self.mmIndent -= 1
        self.writeMm("}")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (id) copyWithZone
        self.writeMm("- (id) copyWithZone: (NSZone *) zone")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("{} * __newList = [[[self class] allocWithZone: zone] init];".format(listName))
        self.writeMm("for (id __obj in _data)")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("id __newObj = [__obj copy];")
        self.writeMm("[[__newList data] addObject: __newObj];")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm("return __newList;")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm("@end")
        self.writeMm()
        self.writeMm()

    def _basicToObjectExpr(self, dataType, varName):
        if dataType.name in ("bool", "byte", "short", "int", "long", "float", "double"):
            return "[NSNumber numberWith{}: {}]".format(dataType.name.capitalize(), varName)
        if dataType.name == "enum":
            return "[NSNumber numberWithInt: {}".format(varName)

        return varName

    def _objectToBasicExpr(self, dataType, varName):
        if dataType.name in ("bool", "byte", "short", "int", "long", "float", "double"):
            return "[{} {}Value]".format(varName, dataType.name)
        if dataType.name == "enum":
            return "[{} intValue]".format(varName)

        return varName

    def parseDict(self, dataType):
        dictName = dataType.name
        valType = dataType.valType
        keyType = dataType.keyType

        self.writeHh("// {}".format(dictName))
        self.writeHh("@interface {}: NSObject <GYMessageBaseProtocol>".format(dictName))
        self.writeHh("@property (copy, nonatomic) NSMutableDictionary * data;")
        self.writeHh()
        self.writeHh("- (id) init;")
        self.writeHh("- (void) __read: (GYSerializer *) __is;")
        self.writeHh("- (void) __write: (GYSerializer *) __os;")
        self.writeHh("- (id) copyWithZone: (NSZone *) zone;")
        self.writeHh("@end")
        self.writeHh()
        self.writeHh()

        self.writeMm("@implementation {}".format(dictName))

        # - (id) init
        self.writeMm("- (id) init")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("self = [super init];")
        self.writeMm("if (!self) return self;")
        self.writeMm()
        self.writeMm("_data = [[NSMutableDictionary alloc] init];")
        self.writeMm("return self;")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (void) __read
        self.writeMm("- (void) __read: (GYSerializer *) __is")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("GYInt dataSize = [__is readInt];")
        self.writeMm("for (GYInt i = 0; i < dataSize; ++i)")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("{} __key = {};".format(self.getObjcRef(keyType), self.getInitValue(keyType)))
        self.writeMm("{} __val = {};".format(self.getObjcRef(valType), self.getInitValue(valType)))
        self.writeMm(self.getReadExpr(keyType, "__key"))
        self.writeMm(self.getReadExpr(valType, "__val"))

        self.writeMm("[_data setObject: {} forKey: {}];".format(
            self._basicToObjectExpr(valType, "__val"), self._basicToObjectExpr(keyType, "__key"))
        )
        self.mmIndent -= 1
        self.writeMm("}")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (void) __write
        self.writeMm("- (void) __write: (GYSerializer *) __os")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("GYInt dataSize = (GYInt)[_data count];")
        self.writeMm("[__os writeInt: dataSize];")
        self.writeMm("for (id __key in [_data keyEnumerator])")
        self.writeMm("{")
        self.mmIndent += 1
        varExpr = self._objectToBasicExpr(keyType, "__key")
        self.writeMm(self.getWriteExpr(keyType, varExpr))
        self.writeMm()
        self.writeMm("id __val = [_data objectForKey: __key];")
        varExpr = self._objectToBasicExpr(valType, "__val")
        self.writeMm(self.getWriteExpr(valType, varExpr))
        self.mmIndent -= 1
        self.writeMm("}")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (id) copyWithZone
        self.writeMm("- (id) copyWithZone: (NSZone *) zone")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("{} * __newDict = [[[self class] allocWithZone: zone] init];".format(dictName))
        self.writeMm("for (id __key in [_data keyEnumerator])")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("id __newKey = [__key copy];")
        self.writeMm("id __val = [_data objectForKey: __key];")
        self.writeMm("id __newVal = [__val copy];")
        self.writeMm("[[__newDict data] setObject: __newVal forKey: __newKey];")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm("return __newDict;")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm("@end")
        self.writeMm()
        self.writeMm()

    def parseInterface(self, dataType):
        for method in dataType.methodList:
            self.parseResponse(dataType, method)

        self.parseProxy(dataType)

    def _getResponseMethodSignature(self, fields):
        res = "onResponse"
        isFirst = True

        for field in fields:
            paraName = ""
            if isFirst:
                paraName = "With"
                isFirst = False
            else:
                paraName = " and"
            paraName += field.name[0].capitalize() + field.name[1:]
            paraName += ": "
            paraName += "({}) {}".format(self.getObjcRef(field.type), field.name)
            res += paraName

        return res

    def _getResponseMethodCall(self, fields):
        res = "onResponse"
        isFirst = True

        for field in fields:
            paraName = ""
            if isFirst:
                paraName = "With"
                isFirst = False
            else:
                paraName = " and"
            paraName += field.name[0].capitalize() + field.name[1:]
            paraName += ": "
            paraName += "{}".format(field.name)
            res += paraName

        return res

    def _getResponseMethodFullName(self, fields):
        return "- (void) " + self._getResponseMethodSignature(fields)

    def _getCallMethodFullName(self, interfaceName, method):
        responseName = "{}_{}_response".format(interfaceName, method.name)
        res = "- (void) {}WithResponse: ({} *) __response".format(method.name, responseName)

        for field in method.infields:
            paraName = " and"
            paraName += field.name[0].capitalize() + field.name[1:]
            paraName += ": "
            paraName += "({}) {}".format(self.getObjcRef(field.type), field.name)
            res += paraName

        return res

    def parseResponse(self, interfaceType, method):
        methodName = method.name
        interfaceName = interfaceType.name
        className = "{}_{}_response".format(interfaceName, methodName)

        self.writeHh("// {}".format(className))
        self.writeHh("@interface {}: GYRmiResponseBase".format(className))
        self.writeHh("- (id) init;")
        self.writeHh("")
        self.writeHh("#pragma mark - overridden methods")
        self.writeHh("- (void) __onResponse: (GYSerializer *) __is;")
        self.writeHh("- (void) __onError: (NSString *) what code: (int) code;")
        self.writeHh("- (void) __onTimeout;")
        self.writeHh()
        self.writeHh("#pragma mark - class-special methods")
        self.writeHh(self._getResponseMethodFullName(method.outfields) + ";")
        self.writeHh("- (void) onError: (NSString *) what code: (GYInt) code;")
        self.writeHh("- (void) onTimeout;")
        self.writeHh("@end")
        self.writeHh()
        self.writeHh()

        self.writeMm("@implementation " + className)

        # - (id) init
        self.writeMm("- (id) init")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("self = [super init];")
        self.writeMm("return self;")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (void) __onResponse
        self.writeMm("- (void) __onResponse: (GYSerializer *) __is")
        self.writeMm("{")
        self.mmIndent += 1
        for field in method.outfields:
            self.writeMm("{} {} = {};".format(self.getObjcRef(field.type), field.name, self.getInitValue(field.type)))
            self.writeMm(self.getReadExpr(field.type, field.name))
            self.writeMm()
        self.writeMm("[self {}];".format(self._getResponseMethodCall(method.outfields)))
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (void) __onError
        self.writeMm("- (void) __onError: (NSString *) what code: (GYInt) code")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("[self onError: what code: code];")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (void) __onTimeout
        self.writeMm("- (void) __onTimeout")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("[self onTimeout];")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        # - (void) onResponse
        self.writeMm(self._getResponseMethodFullName(method.outfields))
        self.writeMm("{")
        self.writeMm("    // todo:")
        self.writeMm("    // override this method in subclasses")
        self.writeMm("}")
        self.writeMm()

        # - (void) onError
        self.writeMm("- (void) onError: (NSString *) what code: (GYInt) code")
        self.writeMm("{")
        self.writeMm("    // todo:")
        self.writeMm("    // override this method in subclasses")
        self.writeMm("}")
        self.writeMm()

        # - (void) onTimeout
        self.writeMm("- (void) onTimeout")
        self.writeMm("{")
        self.writeMm("    // todo:")
        self.writeMm("    // override this method in subclasses")
        self.writeMm("}")

        self.writeMm("@end")
        self.writeMm()
        self.writeMm()

    def parseProxy(self, interfaceType):
        className = interfaceType.name + "Proxy"
        self.writeHh("// " + className)
        self.writeHh("@interface {}: GYRmiProxyBase".format(className))
        self.writeHh("- (id) init;")
        self.writeHh()

        self.writeMm("@implementation {}".format(className))

        # - (id) init
        self.writeMm("- (id) init")
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("self = [super initWithName: @\"{}\"];".format(interfaceType.name))
        self.writeMm("return self;")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()

        for method in interfaceType.methodList:
            self.parseMethod(interfaceType.name, method)

        self.writeHh("@end")
        self.writeHh()
        self.writeHh()

        self.writeMm("@end")
        self.writeMm()
        self.writeMm()

    def parseMethod(self, interfaceName, method):
        # declaration
        self.writeHh(self._getCallMethodFullName(interfaceName, method) + ";")

        # definition
        self.writeMm(self._getCallMethodFullName(interfaceName, method))
        self.writeMm("{")
        self.mmIndent += 1
        self.writeMm("GYSerializer * __os = [[GYSerializer alloc] init];")
        self.writeMm("[__os startToWrite];")
        self.writeMm("[__os writeByte: GYRmiDataCall];")
        self.writeMm("[__os writeString: [self name]];")
        self.writeMm("[__os writeString: @\"{}\"];".format(method.name))
        self.writeMm()
        self.writeMm("GYInt __msgId = [GYRmiProxyBase getMsgId];")
        self.writeMm("[__os writeInt: __msgId];")
        self.writeMm("[__response setMsgId: __msgId];")

        if method.infields:
            self.writeMm()

        for field in method.infields:
            self.writeMm(self.getWriteExpr(field.type, field.name));

        self.writeMm()
        self.writeMm("[self invoke: __os withCallback: __response];")
        self.mmIndent -= 1
        self.writeMm("}")
        self.writeMm()


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
