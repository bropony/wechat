"""
* @name runtest.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:56
*
* @desc runtest.py
"""

from gamit.log.logger import Logger

from core.enginehelper import EngineHelper
from message.gate import gatemsg
from message.gate import command

def runTest():
    Logger.logInfo("Sending out first message")
    data = gatemsg.SMessage()
    EngineHelper.client.sendMessage(command.FirstMessage, [], data)
