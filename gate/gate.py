"""
* @name gate.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/3 10:26
*
* @desc gate.py
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

from optparse import OptionParser

def main():
    optParser = OptionParser()
    optParser.add_option("-c", "--channel-id", type="int", dest="channelId")
    options, args = optParser.parse_args()
    channelId = options.channelId or 0

    #load server configs
    ServerConfigManager.loadConfig()

    # start logger
    logDirName = "log/gate"
    if channelId > 0:
        logDirName = "{}-{}".format(logDirName, channelId)

    loggerDir = os.path.join(os.getcwd(), logDirName)
    Logger.startLogging(loggerDir, ServerConfigManager.isDebug)

    Logger.logInfo("loading configs...")
    staticdata.dataloader.loadConfigs()

    app = Application(channelId)

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