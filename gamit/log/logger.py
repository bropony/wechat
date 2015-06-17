#
# logger
#

from twisted.python import log
#from twisted.python.logfile import DailyLogFile
import sys
import logging
import os.path
import datetime

class Logger:
    def __init__(self):
        raise Exception("Logger is a singleton, cannot be instantiated.")

    _logger = log
    _logLevel = logging.DEBUG
    _logfile = None
    _logdir = None
    _logfilepath = ""
    _logObserver = None

    @classmethod
    def startLogging(cls, logDir, isDebug):
        if not isDebug:
            cls._logLevel = logging.INFO

        #cls._logger.FileLogObserver(sys.stdout).start()
        cls._logdir = logDir
        cls.updateLogFile()

    @classmethod
    def updateLogFile(cls):
        if not cls._logdir:
            return

        dt = datetime.datetime.now()
        filename = "{:04d}-{:02d}-{:02d}_{:02d}_{:02d}.log".format(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        if filename != cls._logfilepath:
            if cls._logfile:
                #cls._logger.removeObserver(cls._logObserver)
                cls._logfile.close()

            if not os.path.exists(cls._logdir):
                os.makedirs(cls._logdir)

            cls._logfile = open(os.path.join(cls._logdir, filename), "a")
            cls._logfilepath = filename

            #cls._logObserver = cls._logger.FileLogObserver(sys.stdout)
            #cls._logObserver.start()
            cls._logger.startLogging(cls._logfile)

    @classmethod
    def logDebug(cls, *argv):
        if cls._logLevel > logging.DEBUG:
            return

        cls.updateLogFile()

        if not cls._logfile:
            sys.stdout.write(*argv)
            sys.stdout.write("\n")
        else:
            cls._logger.msg(*argv, logLevel=logging.DEBUG)

    @classmethod
    def logInfo(cls, *argv):
        cls.updateLogFile()

        if not cls._logfile:
            sys.stdout.write(*argv)
            sys.stdout.write("\n")
        else:
            cls._logger.msg(*argv, logLevel=logging.INFO)

    @classmethod
    def log(cls, *argv, logLevel=logging.INFO):
        cls.updateLogFile()

        if not cls._logfile:
            sys.stdout.write(*argv)
            sys.stdout.write("\n")
        else:
            cls._logger.msg(*argv, logLevel=logLevel)

