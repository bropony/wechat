"""
* @name dbcache.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/9 19:26
*
* @desc dbcache.py
"""

import os
import sys

# add parent dir to searching paths
main_dir, _ = os.path.split(__file__)
parent_dir, _ = os.path.split(main_dir)
sys.path.append(parent_dir)

import staticdata.dataloader
from staticdata.serverconfig import ServerConfigManager
from gamit.log.logger import Logger
from gamit.mongodb.database import MongoDatabase
from gamit.timer.schedule import Scheduler

from application import Application
from logic.timer.ticker import Ticker

def main():
    #load server configs
    ServerConfigManager.loadConfig()

    # start logger
    loggerDir = os.path.join(os.getcwd(), "log/dbcache")
    Logger.startLogging(loggerDir, ServerConfigManager.isDebug)

    Logger.logInfo("loading configs...")
    if not staticdata.dataloader.loadConfigs():
        return

    Logger.logInfo("Init db connection")
    connConfig = os.path.join(parent_dir, "config/dbcache_connection_config.xml")
    tableConfig = os.path.join(parent_dir, "staticdata/dbconfig/main_db_config.xml")
    if not MongoDatabase.loadConfig(connConfig, tableConfig):
        return

    app = Application()

    Logger.logInfo("initiating app...")
    if app.init():
        Logger.logInfo("starting app...")
        app.start()
        Scheduler.schedule(Ticker(), None, 0.3, 0.3)
    else:
        raise Exception("Initiating Application Failed.")

    Logger.logInfo("stopping app...")
    app.stop()

if __name__ == "__main__":
    main()