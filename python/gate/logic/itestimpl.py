"""
* @name itestimpl.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/5 11:18
*
* @desc itestimpl.py
"""

from message.gate import gatemsg
from message.gate import itest
from message.common import publicdef
from message.gate import command

from gamit.message.messagemanager import MessageManager

class ItestImpl(itest.ITestServant):
    def __init__(self, name):
        super().__init__(name)

    def getIntList(self, size, __request):
        res = publicdef.SeqInt()
        for _ in range(size):
            res.append(_)
        __request.response(res)

        MessageManager.broadcast(command.ETestCommand.FirstMessage, gatemsg.SMessage())

    def getDictIntString(self, size, __request):
        res = {}
        for i in range(size):
            res[i] = str(i)

        __request.response(res)

    def getFloatList(self, size, __request):
        res = []
        for i in range(size):
            res.append(i * 1.1)

    def signup(self, signup, __request):
        #raise Exception("Deprecated Method", 0)
        pass