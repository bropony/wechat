"""
* @name sessionmanager.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/5 19:58
*
* @desc sessionmanager.py
"""

from gamit.singleton.singleton import Singleton

class SessionManager(Singleton):
    _sessionMap = {}

    @classmethod
    def addSession(cls, channelType, session):
        cls._sessionMap[channelType] = session

    @classmethod
    def getSession(cls, channelType):
        if channelType in cls._sessionMap:
            return cls._sessionMap[channelType]

    @classmethod
    def getSessionMap(cls):
        return cls._sessionMap