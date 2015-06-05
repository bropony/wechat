"""
* @name enginehelper
*
* @author ahda86@gmail.com
*
* @date 2015/6/5 11:42
*
* @desc enginehelper
"""

from gamit.singleton.singleton import Singleton

class EngineHelper(Singleton):
    client = None
    messageManager = None

    @classmethod
    def setClient(cls, client):
        cls.client = client

    @classmethod
    def setMessageManager(cls, mgr):
        cls.messageManager = mgr