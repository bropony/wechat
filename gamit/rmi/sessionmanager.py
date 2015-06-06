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
from twisted.internet import reactor


class SessionManager(Singleton):
    _sessionMap = {}
    _interval = 10

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

    @classmethod
    def startHeartBeats(cls, interval=None):
        if interval and interval > 0:
            cls._interval = interval

        reactor.callLater(cls._interval, cls._heartbeats)

    @classmethod
    def _heartbeats(cls):
        for _, s in cls._sessionMap.items():
            s.heartbeat()

        reactor.callLater(cls._interval, cls._heartbeats)