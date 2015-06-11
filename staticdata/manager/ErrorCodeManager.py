"""
* @name ErrorCodeManager.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/11 14:48
*
* @desc ErrorCodeManager.py
"""

from staticdata.loader.manager import *
from message.tables.TErrorConfig import SeqTErrorConfigFromJson

class __ErrorCodeManager(ManagerBase):
    def __init__(self):
        super().__init__(SeqTErrorConfigFromJson)

    def loadConfig(self, filepath):
        configs = loadfile(filepath, self.loader)
        self.data = {}

        for config in configs:
            self.data[config.errorName] = config

        return True

    def findErrorConfig(self, errorName):
        return self.data.get(errorName)

    def raiseError(self, errorName):
        if errorName not in self.data:
            raise Exception(errorName, 0)

        config = self.data[errorName]
        print(config.errorStr, ", ", config.errorCode)
        raise Exception(config.errorStr, config.errorCode)

# manager instance
ErrorCodeManager = __ErrorCodeManager()
