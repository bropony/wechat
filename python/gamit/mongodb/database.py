"""
* @name database.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/9 10:53
*
* @desc database.py
"""

from pymongo import MongoClient
import xml.etree.ElementTree as xmlParser

from gamit.mongodb.table import MongoTable

from gamit.log.logger import Logger

class __Database:
    def __call__(self):
        return self

    def __init__(self):
        self.mongo = None
        self.collection = None
        self.dbname = ""
        self.dbuser = ""
        self.dbpasswd = ""
        self.dbip = ""
        self.dbport = 0
        self.tableMap = {}

    def loadConfig(self, connectionConfig, tableConfig):
        if not self.__initDatabase(connectionConfig):
            return False

        if not self.__initTables(tableConfig):
            return False

        return True

    def findTable(self, tableName):
        return self.tableMap.get(tableName)

    def findTableByMessageTypeName(self, msgName):
        return self.tableMap.get(msgName)

    def findTableByMessageObj(self, msgObj):
        return self.tableMap.get(msgObj.__class__.__name__)

    def findTableByMessageType(self, msgType):
        return self.tableMap.get(msgType.__name__)

    def start(self):
        self.mongo = MongoClient(self.dbip, self.dbport)
        if self.dbuser:
            self.mongo[self.dbname].authenticate(self.dbuser, self.dbpasswd, mechanism="SCRAM-SHA-1")
        self.collection = self.mongo[self.dbname]

        for _, table in self.tableMap.items():
            if not table.initTable(self.collection):
                return False

        return True

    def stop(self):
        self.tableMap = {}
        self.mongo.close()

    def __initDatabase(self, config):
        xml = xmlParser.parse(config)
        for child in xml.getroot():
            tag = child.tag
            text = child.text
            if tag == 'name':
                self.dbname = text
            elif tag == 'ip':
                self.dbip = text
            elif tag == 'port':
                self.dbport = int(text)
            elif tag == 'username':
                self.dbuser = text
            elif tag == 'passwd':
                self.dbpasswd = text

        if not self.dbname:
            Logger.logInfo("__Database.__initDatabase", "database name not specified")
            return False

        if not self.dbip:
            self.dbip = "127.0.0.1"

        if not self.dbport:
            self.dbport = 27017

        return True

    def __initTables(self, config):
        xml = xmlParser.parse(config)
        for child in xml.getroot():
            tag = child.tag
            attrib = child.attrib
            if tag != "table":
                continue

            if not self.__addTableConfig(attrib):
                return False

        return True

    def __addTableConfig(self, attrib):
        name = ""
        name_key = "name"
        if name_key not in attrib:
            Logger.logInfo("__Database.__initDatabase", "table name not specified")
            return False
        else:
            name = attrib[name_key]

        struct = ""
        structKey = "struct"
        if structKey in attrib:
            struct = attrib[structKey]

        index = ""
        index_key = "index"
        if index_key in attrib:
            index = attrib[index_key]

        insertOnly = False
        insert_only_key = "insert_only"
        if insert_only_key in attrib:
            insertOnly = attrib[insert_only_key]
            if insertOnly.upper() == "TRUE":
                insertOnly = True
            else:
                insertOnly = False

        if not insertOnly and not index:
            Logger.logInfo("__Database.__initDatabase", "index must be specified for non-write-only tables")
            return False

        table = MongoTable(name, struct, index, insertOnly)
        self.tableMap[name] = table
        self.tableMap[struct] = table

        return True
# end of __Database

MongoDatabase = __Database()
