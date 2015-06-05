"""
* @name ItestTest.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:56
*
* @desc ItestTest.py
"""

from message.gate.itest import *
from core.enginehelper import EngineHelper

class ITest_Getintlist_Response_Impl(ITest_Getintlist_Response):
    def onResponse(self, intList):
        print("ITest_Getintlist_Response_Impl.onResponse", intList)

    def onError(self, what, code):
        print("onError:", what, code)

class ITest_Signup_Response_Impl(ITest_Signup_Response):
    def onResponse(self, loginReturn):
        print("ITest_Signup_Response_Impl.onResponse", loginReturn)

    def onError(self, what, code):
        print("onError:", what, code)