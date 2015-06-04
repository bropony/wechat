"""
* @name servant.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 10:30
*
* @desc servant.py
"""

from gamit.singleton.singleton import Singleton
from message.gate.itest import ITestServant

class ServantSetting(Singleton):
    @staticmethod
    def initServant(server):
        server.addServant(ITestServant("ITest"))