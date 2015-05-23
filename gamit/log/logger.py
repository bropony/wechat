#
# logger
#

from twisted.python import log
from twisted.python.logfile import DailyLogFile
import logging
import os.path

class Logger:
    def __init__(self):
        raise Exception("Logger is a singleton, cannot be instantiated.")

    _logger = log
    _logLevel = logging.DEBUG

    @classmethod
    def startLogging(cls, logDir, isDebug):
        if not isDebug:
            _logLevel = logging.INFO
            
        logFile = DailyLogFile.fromFullPath(os.path.join(logDir, "log.txt"))
        log.startLogging(logFile)

    @classmethod
    def logDebug(cls, *argv):
        if cls._logLevel > logging.DEBUG:
            return

        cls._logger.msg(*argv, logLevel=logging.DEBUG)

    @classmethod
    def logInfo(cls, *argv):
        cls._logger.msg(*argv, logLevel=logging.INFO)

    @classmethod
    def log(cls, *argv, logLevel=logging.INFO):
        cls._logger.msg(*argv, logLevel=logLevel)

