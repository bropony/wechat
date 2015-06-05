__author__ = 'mahanzhou'

from gamit.message.commandhandler import CommandHandlerBase
from gamit.message.message import MessageBlock
from gamit.log.logger import Logger

class NotACommandHandlerError(Exception):
    pass

class MessageManager:
    def __init__(self, server):
        self.rmiServer = server
        self.handlerMap = {}
        self.idHandlerMap = {}

    def addCommandHandler(self, command, handler):
        if not issubclass(handler.__class__, CommandHandlerBase):
            raise NotACommandHandlerError()

        Logger.logDebug("Registering Command: ", command)
        self.handlerMap[command] = handler

    def addCommandHandlerById(self, id, handler):
        if not issubclass(id, CommandHandlerBase):
            raise NotACommandHandlerError()

        self.idHandlerMap[id] = handler

    def broadcast(self, command, data):
        try:
            toIdList = []
            msg = MessageBlock(command, toIdList, data)
            self.rmiServer.broadcast(msg.getOsBuffer())
        except Exception as ex:
            Logger.logInfo(ex.__traceback__)

    def sendMessage(self, connId, command, toIdList, data):
        try:
            msg = MessageBlock(command, toIdList, data)
            self.rmiServer.send(connId, msg.getOsBuffer())
        except Exception as ex:
            Logger.logInfo(ex.__traceback__)

    def onMessage(self, _is):
        try:
            msg = MessageBlock(_is)
            command = msg.command
            processed = False
            for id in msg.toIdList:
                if id in self.idHandlerMap:
                    self.idHandlerMap[id].onMessage(command, msg.toIdList, msg.data)
                    processed = True

            if not processed:
                if command in self.handlerMap:
                    self.handlerMap[command].onMessage(command, msg.toIdList, msg.data)
                else:
                    Logger.logDebug("MessageManager.onMessage", "Command not found:", command)

        except Exception as ex:
            Logger.logInfo(ex.__traceback__)
#end of MessageManager