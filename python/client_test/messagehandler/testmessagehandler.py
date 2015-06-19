"""
* @name testmessagehandler.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:26
*
* @desc testmessagehandler.py
"""

from gamit.message.commandhandler import CommandHandlerBase

class TestMessageHandler(CommandHandlerBase):
    def onMessage(self, command, toIdList, data):
        print("message received: ", command)
        for key, val in data.__dict__.items():
            print("{}: {}".format(key, val))
#####