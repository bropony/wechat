__author__ = 'mahanzhou'

import abc
import datetime

class TimerBase(metaclass=abc.ABCMeta):
    _timerId = 0

    def __init__(self):
        self._id = self.__class__._timerId
        self.__class__._timerId += 1

    def getId(self):
        return self._id

    @abc.abstractmethod
    def onTimeout(self, data):
        pass

class TimerProxy:
    def __init__(self, timer, data, future, interval):
        self.timer = timer
        self.data = data
        self.future = future
        self.scheduledTimes = 0
        self.interval = interval

    def handleTimeout(self):
        now = datetime.datetime.now()
        if now >= self.future:
            self.timer.onTimeout(self.data)
            self.scheduledTimes += 1

        if self.interval.total_seconds() >= 0:
            while self.future <= now:
                self.future += self.interval
            return True
        else:
            return False
#####