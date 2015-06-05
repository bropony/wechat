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
from gamit.serialize.serializer import Serializer

from core.enginehelper import EngineHelper
from message.gate import gatemsg
from message.gate.command import ETestCommand

def runTest():
    Logger.logInfo("Sending out first message")
    data = gatemsg.SMessage()
    __os = Serializer()
    data.__write(__os)

    # EngineHelper.client.sendMessage(ETestCommand.FirstMessage, [], data)
