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

from test.ItestTest import ITest_Getintlist_Response_Impl, ITest_Signup_Response_Impl

def runTest():
    #Logger.logInfo("Sending out first message")
    #data = gatemsg.SMessage()
    #EngineHelper.client.sendMessage(ETestCommand.FirstMessage, [], data)

    Logger.logInfo("calling getIntList")
    proxy = EngineHelper.client.getProxy("ITest")
    if proxy:
        reponse = ITest_Getintlist_Response_Impl()
        proxy.getIntList(reponse, 10)

        xxx = ITest_Signup_Response_Impl()
        proxy.signup(xxx, gatemsg.SSignup())