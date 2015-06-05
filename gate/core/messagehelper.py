"""
* @name messagehelper
*
* @author ahda86@gmail.com
*
* @date 2015/6/5 11:30
*
* @desc messagehelper
"""

from gamit.singleton.singleton import Singleton

class MessageHelper(Singleton):
    messageManager = None

    @classmethod
    def setMessageManager(cls, mgr):
        cls.messageManager = mgr
