__author__ = 'mahanzhou'

from gamit.timer.timerbase import TimerProxy, TimerBase
from twisted.internet import reactor
import datetime

SECS_OF_A_DAY = 24 * 3600

class __Scheduler:
    def __call__(self):
        return self

    def __init__(self):
        self.timerMap = {}

    def schedule(self, timer, data, future, interval):
        """
        :brief register and schedule a timer
        :param timer: instance of class subclasses from TimerBase with onTimeout overwrite
        :param data: user data in future use. This data will be passed to timer.onTimeout.
        :param future: @future indicates a latter moment the first onTimeout is called.
                        four type of obj supported.
                        int or float obj indicates number of seconds since now to @future
                        datetime.datetime indicates the datetime of @future
                        datetime.timedelta indicates a time period since now to @future
        :param interval: how often in second timer.onTimeout is called.
        :return (ok, reason) When @ok is True, @reason is set to ''.
                            And timer is successfully registered.
                            When @ok is False, timer is not successfully registered by some @reason
        """
        if not issubclass(timer.__class__, TimerBase):
            return False, "Invalid type of timer. Obj of classes that subclass from TimerBase required."

        if isinstance(future, float) or isinstance(future, int):
            future = datetime.datetime.now() + datetime.timedelta(0, future)
        elif isinstance(future, datetime.timedelta):
            future = datetime.datetime.now() + future
        elif not isinstance(future, datetime.datetime):
            return False, "Invalid type of future. Obj of int, float, timedelta or datetime required"

        if isinstance(interval, int) or isinstance(interval, float):
            days = int(interval) % SECS_OF_A_DAY
            secs = interval - days * SECS_OF_A_DAY
            interval = datetime.timedelta(days, secs)
        elif not isinstance(interval, datetime.timedelta):
            return False, "Invalid type of interval. A number required"

        timerPrx = TimerProxy(timer, data, future, interval)
        self.timerMap[timer.getId()] = timerPrx

        return True, ""

    def cancel(self, timer):
        if timer.getId() in self.timerMap:
            del self.timerMap[timer.getId()]

    def start(self):
        self._loop()

    def _loop(self):
        newMap = {}
        print(self.timerMap)
        for timerId, timerPrx in self.timerMap.items():
            if timerPrx.handleTimeout():
                newMap[timerId] = timerPrx

        self.timerMap = newMap

        reactor.callLater(0.03, self._loop)

Scheduler = __Scheduler()
####