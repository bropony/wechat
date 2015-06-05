"""
* @name client_test.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:18
*
* @desc client_test.py
"""

import sys
import os
import os.path

# add parent dir to searching paths
main_dir, _ = os.path.split(__file__)
parent_dir, _ = os.path.split(main_dir)
sys.path.append(parent_dir)

# imports
import staticdata.dataloader
from staticdata.serverconfig import ServerConfigManager
from gamit.log.logger import Logger

from application import Application


def main():
    ServerConfigManager.loadConfig()

    # start logger
    loggerDir = os.path.join(os.getcwd(), "log")
    if not os.path.exists(loggerDir):
        os.mkdir(loggerDir)
    Logger.startLogging(loggerDir, ServerConfigManager.isDebug)

    Logger.logInfo("loading configs...")
    staticdata.dataloader.loadConfigs()

    app = Application()

    Logger.logInfo("initiating app...")
    if app.init():
        Logger.logInfo("starting app...")
        app.start()
    else:
        raise Exception("Initiating Application Failed.")

    Logger.logInfo("stopping app...")
    app.stop()

if __name__ == "__main__":
    main()