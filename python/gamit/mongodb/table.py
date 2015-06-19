"""
* @name table.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/9 15:24
*
* @desc table.py
"""
from pymongo import ASCENDING
from gamit.message.message import MessageBlock
from gamit.log.logger import Logger

class MongoTable:
    def __init__(self, name, msgName, index, insert_only):
        self.table = None
        self.name = name
        self.msgName = msgName
        self.index = index
        self.insertOnly = insert_only

        if not self.msgName:
            self.msgName = self.name

        self.msgType = MessageBlock.findMessageType(self.msgName)

    def initTable(self, db):
        if not self.msgType:
            Logger.logInfo("struct {} is not defined".format(self.msgName))
            return False

        if not self.name in db.collection_names():
            if self.index:
                db[self.name].create_index([(self.index, ASCENDING)])

        self.table = db[self.name]
        return True

    def raiseError(self, ex):
        what = "DBError: " + ex.args[0]
        code = 10000
        raise Exception(what, code)

    def findMany(self, key):
        try:
            res = []
            for doc in self.table.find({self.index: key}):
                msg = self.msgType()
                msg._fromJson(doc)
                res.append(msg)
            return res
        except Exception as ex:
            self.raiseError(ex)

    def findOne(self, key):
        try:
            doc = self.table.find_one({self.index: key})
            if doc:
                res = self.msgType()
                res._fromJson(doc)
                return res

            return None
        except Exception as ex:
            self.raiseError(ex)

    def findManyWithQuey(self, query):
        try:
            res = []
            if not isinstance(query, dict):
                return res

            for doc in self.table.find(query):
                msg = self.msgType()
                msg._fromJson(doc)
                res.append(msg)
            return res
        except Exception as ex:
            self.raiseError(ex)

    def findOneWithQuery(self, query):
        if not isinstance(query, dict):
            return None

        try:
            doc = self.table.find_one(query)
            if doc:
                msg = self.msgType()
                msg._fromJson(doc)
                return msg

            return None
        except Exception as ex:
            self.raiseError(ex)

    def update(self, data):
        if not isinstance(data, list) and not isinstance(data, tuple):
            data = [data]

        try:
            docs = []
            for rec in data:
                if not isinstance(rec, self.msgType):
                    raise Exception("Not all record passed in a instance of {}".format(self.msgType.name))
                docs.append(rec._toJson())

            if self.insertOnly:
                self.table.insert_manay(docs)
            else:
                for doc in docs:
                    self.table.replace_one({self.index: doc[self.index]}, doc, upsert=True)
        except Exception as ex:
            self.raiseError(ex)

    def updateWithQuery(self, filter, update, upsert, update_one=False):
        try:
            if update_one:
                self.table.update_one(filter, update, upsert)
            else:
                self.table.update_many(filter, update, upsert)
        except Exception as ex:
            self.raiseError(ex)

    def save(self, data):
        if not isinstance(data, list) and not isinstance(data, tuple):
            data = [data]

        try:
            docs = []
            for rec in data:
                if not isinstance(rec, self.msgType):
                    raise Exception("Not all record passed in a instance of {}".format(self.msgType.name))
                docs.append(rec._toJson())

            self.table.insert_many(docs)
        except Exception as ex:
            self.raiseError(ex)

    def delete(self, filter, delete_one=False):
        try:
            if delete_one:
                self.table.delete_one(filter)
            else:
                self.table.delete_manay(filter)
        except Exception as ex:
            self.raiseError(ex)
# end of class Table
