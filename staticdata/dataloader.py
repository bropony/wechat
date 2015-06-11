"""
* @name dataloader.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/3 11:00
*
* @desc dataloader.py
"""

import os
__mydir = os.path.split(__file__)[0]
__datadir = os.path.join(__mydir, "data")

if __name__ == "__main__":
    import sys
    parent_dir = os.path.split(__mydir)[0]
    sys.path.append(parent_dir)

from gamit.log.logger import Logger

#
# Config Manager imports start here
#
from staticdata.manager.ErrorCodeManager import ErrorCodeManager

def _loadConfig(configManager, filePath):
    Logger.logInfo("Begin of loading {}".format(filePath))
    absPath = os.path.join(__datadir, filePath)

    if not configManager.loadConfig(absPath):
        return False

    Logger.logInfo("End of loading {}".format(filePath))
    return True

def loadConfigs():
    if not _loadConfig(ErrorCodeManager, "t_error_config.json"):
        return False

    return True

if __name__ == "__main__":
    loadConfigs()