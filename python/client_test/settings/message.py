"""
* @name message.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:23
*
* @desc message.py
"""
from message.gate.command import ETestCommand
from messagehandler.testmessagehandler import TestMessageHandler
from gamit.singleton.singleton import Singleton
from gamit.message.messagemanager import MessageManager

class MessageSetting(Singleton):
    @staticmethod
    def initMessangeHandler():
        MessageManager.addCommandHandler(ETestCommand.FirstMessage, TestMessageHandler())

