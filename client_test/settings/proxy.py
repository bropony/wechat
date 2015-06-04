"""
* @name proxy.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:23
*
* @desc proxy.py
"""
from gamit.singleton.singleton import Singleton
from message.gate.itest import ITestProxy

class ProxySetting(Singleton):
    @staticmethod
    def initGateProxy(client):
        client.addProxy(ITestProxy("ITest"))

#