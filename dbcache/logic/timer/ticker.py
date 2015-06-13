"""
* @name ticker
*
* @author ahda86@gmail.com
*
* @date 2015/6/13 11:19
*
* @desc ticker
"""

from gamit.timer.timerbase import TimerBase

class Ticker(TimerBase):
    def __init__(self):
        super().__init__()
        self.ticks = 0

    def onTimeout(self, data):
        self.ticks += 1
        print("Ticks: ", self.ticks)
#####