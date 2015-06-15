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
from gamit.message.messagemanager import MessageManager

class TestMessageHandler(CommandHandlerBase):
    def onMessage(self, command, toIdList, data):
        print("message received: ", command)
        for key in data.__slots__:
            print("{}: {}".format(key, data[key]))

        MessageManager.broadcast(command, data)

#