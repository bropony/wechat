"""
* @name testmessagehandler
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 15:58
*
* @desc testmessagehandler
"""

from gamit.message.commandhandler import CommandHandlerBase
from core.messagehelper import MessageHelper

class TestMessageHandler(CommandHandlerBase):
    def onMessage(self, command, toIdList, data):
        print("message received: ", command)
        for key, val in data.__dict__:
            print("{}: {}".format(key, val))

        MessageHelper.messageManager.broadcast(command, data)

#