"""
* @name loader.py
*
* @author ahda86@gmail.com
*
* @date 2015/5/27 20:02
*
* @desc loader.py
"""

import os.path
import  re

class TypeBase:
    def __init__(self, scope, name):
        self.scope = scope
        self.name = name

        if scope:
            self.fullname = scope + "." + name
        else:
            self.fullname = name


class BasicType(TypeBase):
    def __init__(self, name, type):
        super().__init__("", name)
        self.type = type

class Field:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Struct(TypeBase):
    def __init__(self, scope, name):
        super().__init__(scope, name)
        self.fields = []
        self.nameSet = set()

    def addField(self, fieldName, fieldType):
        if fieldName in self.nameSet:
            return 'multi-definition of field {}.{}'.format(self.name, fieldName)
        f = Field(fieldName, fieldType)
        self.fields.append(f)
        self.nameSet.add(fieldName)

class Enum(TypeBase):
    def __init__(self, scope, name):
        super().__init__(scope, name)
        self.pairs = []
        self.valSet = set()
        self.nameSet = set()

    def addVal(self, name, value):
        if name in self.nameSet:
            return 'multi-definition of field {}.{}'.format(self.name, name)
        if value in self.valSet:
            return '{} is used more than once in {}.{}'.format(value, self.name, name)
        self.nameSet.add(name)
        self.valSet.add(value)
        self.pairs.append((name, value))


class List(TypeBase):
    def __init__(self, scope, name, type):
        super().__init__(scope, name)
        self.type = type


class Dict(TypeBase):
    def __init__(self, scope, name, keyType, valType):
        super().__init__(scope, name)
        self.keyType = keyType
        self.valType = valType


class Method(TypeBase):
    def __init__(self, scope, name):
        super().__init__(scope, name)
        self.infields = []
        self.outfields = []
        self.nameSet = {}

    def parse(self, lines):
        pass


class Interface(TypeBase):
    def __init__(self, scope, name):
        super().__init__(scope, name)
        self.methodList = []

    def addMethod(self, name, lines):
        pass


class Loader:
    def __init__(self, scope, rootdir, relPath, manager):
        self.rootdir = rootdir
        self.relPath = relPath
        self.filepath = os.path.join(rootdir, relPath)
        self.scope = scope
        direct, filename = os.path.split(relPath)
        scopes = [e for e in re.split(r'/', direct) if e]
        self.name, ex = os.path.splitext(filename)
        scopes.append(self.name)
        if scope:
            self.scope += "." + ".".join(scopes)
        else:
            self.scope = ".".join(scopes)

        self.structManager = manager
        self.includeAllowed = True
        self.types = []
        self.typeMap = {}

        self.parsers = dict()
        self.parsers["include"] = self.parseInclude
        self.parsers["struct"] = self.parseStruct
        self.parsers["enum"] = self.parseEnum
        self.parsers["list"] = self.parseList
        self.parsers["dict"] = self.parseDict
        self.parsers["interface"] = self.parseInterface

    def add(self, dataType):
        self.structManager.add(dataType)
        self.types.append(dataType)
        self.typeMap[dataType.name] = dataType

    def find(self, name):
        if name in self.typeMap:
            return self.typeMap[name]
        return None

    @staticmethod
    def readline(fin):
        fin.lno += 1
        line = fin.readline()
        return line

    def raiseExp(self, what):
        raise Exception("{} {}".format(self.relPath, what))

    def raiseSyntaxError(self, lineno):
        self.raiseExp("Syntax error at line %d" % lineno)

    @staticmethod
    def getKeyWord(line):
        m = re.match(r'([a-z]+)', line)
        if m:
            return m.group(1)
        return ""

    def checkVarName(self, word, lno):
        if word[0] in "0123456789":
            self.raiseExp('"{}" is not a valid name at line {}'.format(word, lno))

        if word in ("bool", "byte", "short", "int", "long",
                    "float", "double", "string", "date", "binary",
                    "include", "struct", "enum", "list", "dict", "interface"):
            self.raiseExp('Keyword "{}" is not a valid name at line {}'.format(word, lno))

    @staticmethod
    def clearLine(line):
        if not line:
            return line
        return re.split(r'#', line.rstrip())[0]

    def loadFile(self):
        try:
            fin = open(self.filepath)
            fin.lno = 0
        except Exception as ex:
            self.raiseExp("File does not exist")

        line = self.readline(fin)
        while True:
            if not line:
                break

            line = self.clearLine(line)
            if not line.strip():
                continue

            if re.match(r'^\s+'):
                self.raiseExp("No spaces allowed at beginnig of line %d" % fin.lno)

            line = line.rstrip()
            keyWord = self.getKeyWord(line)

            if keyWord in self.parsers:
                line = self.parsers[keyWord](self, line, fin)
            else:
                self.raiseExp("Syntax error at line %d" % fin.lno)
        # end of while
        fin.close()

    def parseInclude(self, line, fin):
        m = re.match(r'^include\s*"([^"]+)"$')
        if not m:
            self.raiseExp("Syntax error at line %d" % fin.lno)
        file = m.group(1)
        self.structManager.loadFile(file)

        return self.readline(fin)

    def parseStruct(self, line, fin):
        m = re.match("^struct\s+(\w+):$")
        if not m:
            self.raiseSyntaxError(fin.lno)
        structName = m.group(1)
        self.checkVarName(structName, fin.lno)

        struct = Struct(self.scope, structName)
        if self.structManager.find(struct.fullname):
            self.raiseExp("Multi definition of '{}' at line {}".format(structName, fin.lno))

        indentSet = set()
        newLine = ""
        oldLno = fin.lno

        while True:
            newLine = self.readline(fin)
            if not newLine:
                break
            newLine = self.clearLine(newLine)
            if not newLine.strip():
                continue
            m = re.match(r"^(\s+)", newLine)
            if m:
                indentSet.add(m.group(1))
                newLine = newLine.strip()
                re.match(r'^(\w+)\s*(\w+)$')
                if m:
                    fieldTypeName, fieldName = m.group(1), m.group(2)
                    fieldType = self.structManager.find(fieldTypeName, scope=self.scope)
                    if not fieldType:
                        self.raiseExp('"{}" is not defined at line {}'.format(fieldTypeName, fin.lno))
                    self.checkVarName(fieldName, fin.lno)
                    what = struct.addField(fieldName, fieldType)
                    if what:
                        self.raiseExp(what)
                else:
                    self.raiseSyntaxError(fin.lno)
            else:
                break
        # end of while
        if len(indentSet) > 1:
            self.raiseSyntaxError("Indent not consistent between line {} to {}".format(oldLno, fin.lno))

        if len(struct.fields) == 0:
            self.raiseExp("No field defined for struct %s" % structName)

        self.add(struct)
        return newLine

    def parseEnum(self, line, fin):
        m = re.match(r'enum\s+(\w+):$')
        if not m:
            self.raiseSyntaxError(fin.lno)
        enumName = m.group(1)
        self.checkVarName(enumName, fin.lno)

        enum = Enum(self.scope, enumName)
        if self.structManager.find(enum.fullname):
            self.raiseExp("Multi-definition of '{}' at line {}".format(enumName, fin.lno))

        oldLno = fin.lno
        indentSet = set()
        newLine = ""
        while True:
            newLine = self.readline(fin)
            if not line:
                break
            newLine = self.clearLine(line)
            if not newLine.strip():
                continue
            m = re.match(r'^(\s+)')
            if m:
                indentSet.add(m.group(1))
                newLine = newLine.strip()
                m = re.match(r'^(\w+)\s*=\s*(\d+)$')
                if m:
                    fieldName = m.group(1)
                    fieldValue = int(m.group(2))
                    self.checkVarName(fieldName, fin.lno)
                    what = enum.addVal(fieldName, fieldValue)
                    if what:
                        self.raiseExp(what)
                else:
                    self.raiseSyntaxError(fin.lno)
            else:
                break
        # end of while
        if len(indentSet) > 1:
            self.raiseSyntaxError("Indent not consistent between line {} to {}".format(oldLno, fin.lno))

        if len(enum.fields) == 0:
            self.raiseExp("No field defined for struct %s" % enumName)

        self.add(enum)
        return newLine

    def parseList(self, line, fin):
        m = re.match(r'^list\s*<\s*(\w+)\s*>\s*(\w+)$')
        if not m:
            self.raiseSyntaxError(fin.lno)
        dataTypeName = m.group(1)
        varName = m.group(2)
        self.checkVarName(varName, fin.lno)

        dataType = self.find(dataTypeName)
        if not dataType:
            dataType = self.structManager.find(dataTypeName)
        if not dataType:
            self.raiseExp("At line{}: Identifier {} is not found.".format(fin.lno, dataTypeName))

        listT = List(self.scope, varName, dataType)
        if self.structManager.find(listT.fullname):
            self.raiseExp("Multi definition of '{}' at line {}".format(varName, fin.lno))

        self.add(listT)

        return self.readline(fin)

    def parseDict(self, line, fin):
        m = re.match(r'^dict\s*<\s*(\w+)\s*,\s*(\w+)\s*>\s*(\w+)$')
        if not m:
            self.raiseSyntaxError(fin.lno)

        keyTypeName = m.group(1)
        valTypeName = m.group(2)
        varName = m.group(3)

        self.checkVarName(varName, fin.lno)

        if keyTypeName not in ("int", "long", "string"):
            self.raiseExp("At line{}: {} cannot be used as key type.".format(fin.lno, keyTypeName))
        keyType = self.structManager.find(keyTypeName)

        valType = self.find(valTypeName)
        if not valType:
            valType = self.structManager.find(valTypeName)
        if not valType:
            self.raiseExp("At line{}: Identifier {} is not found.".format(fin.lno, valType))

        dictT = Dict(varName, keyType, valType)
        if self.structManager.find(dictT.fullname):
            self.raiseExp("Multi definition of '{}' at line {}".format(varName, fin.lno))

        self.add(dictT)

        return self.readline(fin)

    def parseInterface(self, line, fin):
        m = re.match(r'^interface\s+(\w+):$', line)
        if not m:
            self.raiseSyntaxError(fin.lno)

        interfaceName = m.group(1)
        interface = Interface(self.scope, interfaceName)
        if self.structManager.find(interface.fullname):
            self.raiseExp("Multi-definition of '{}' at line {}".format(interfaceName, fin.lno))

        methodTags = []
        indentSet = set()
        oldLno = fin.lno
        beginOfMethod = False
        while True:
            line = self.readline(fin)
            line = self.clearLine(line)
            if not line:
                continue
            if not line.strip():
                continue

            if not beginOfMethod:
                m = re.search("^(\s+)method\s+(\w+)\s*\(", line)
                if not m:
                    break
                mtg = []
                indentSet.add(m.group(1))
                mtg.append(m.group(2))
                mtg.append(fin.lno)
                mtg.append([line])
                methodTags.append(mtg)
                if ")" in line:
                    beginOfMethod = False
                else:
                    beginOfMethod = True
            elif beginOfMethod:
                methodTags[-1][2].append(line)
                if ")" in line:
                    beginOfMethod = False
        # end of while

        if len(indentSet) > 1:
            self.raiseSyntaxError("Indent not consistent between line {} to {}".format(oldLno, fin.lno))

        for elem in methodTags:
            interface.addMethod(elem[0], elem[1], elem[2])

        self.add(interface)
        return line
    # end of parseInterface
# end of Loader
