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

from gamit.log.logger import Logger

class Database:
    def __init__(self):
        self.mongo = None
        self.dbname = ""
        self.dbuser = ""
        self.dbport = 0
        self.tableMap = {}

    def loadConfig(self, config):
        xml = xmlParser.parse(config)
        dbConfig = xml.find("database")
        if not dbConfig:
            return False
        else:
            if not self.__initDatabase(dbConfig.attrib):
                return False

        for t in xml.findall("table"):
            if not self.__addTableConfig(t.attrib):
                return False

        return True

    def __initDatabase(self, attrib):
        if "name" in attrib:
            self.dbname = attrib["name"]
        else:
            Logger.logInfo("Database.init", "database.name not specified.")
            return False


    def __addTableConfig(self, attrib):
        pass