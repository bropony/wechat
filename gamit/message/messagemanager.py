__author__ = 'mahanzhou'

from gamit.message.commandhandler import CommandHandlerBase
from gamit.message.message import MessageBlock
from gamit.log.logger import Logger
from gamit.rmi.sessionmanager import SessionManager

class NotACommandHandlerError(Exception):
    pass

class __MessageManager:
    def __call__(self, server):
        self.rmiServer = server
        return self

    def __init__(self):
        self.rmiServer = None
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

    def sendMessageToOwnChannel(self, command, toIdList, data):
        self._onMessage(command, toIdList, data)

    def broadcastToAllSessions(self, command, toIdList, data):
        for _, session in SessionManager.getSessionMap().items():
            session.sendMessage(command, toIdList, data)

    def sendMessageToSession(self, channelType, command, toIdList, data):
        session = SessionManager.getSession(channelType)
        if session:
            session.sendMessage(command, toIdList, data)

    def broadcast(self, command, data):
        if not self.rmiServer:
            return

        try:
            toIdList = []
            msg = MessageBlock(command, toIdList, data)
            self.rmiServer.broadcast(msg.getOsBuffer())
        except Exception as ex:
            Logger.logInfo(ex)

    def sendMessage(self, connId, command, toIdList, data):
        if not self.rmiServer:
            return

        try:
            msg = MessageBlock(command, toIdList, data)
            self.rmiServer.send(connId, msg.getOsBuffer())
        except Exception as ex:
            Logger.logInfo(ex)

    def onMessage(self, _is):
        try:
            msg = MessageBlock(_is)
            command = msg.command
            processed = False
            self._onMessage(msg.command, msg.toIdList, msg.data)
        except Exception as ex:
            Logger.logInfo(ex)

    def _onMessage(self, command, toIdList, data):
        try:
            processed = False
            for id in toIdList:
                if id in self.idHandlerMap:
                    self.idHandlerMap[id].onMessage(command, toIdList, data)
                    processed = True

            if not processed:
                if command in self.handlerMap:
                    self.handlerMap[command].onMessage(command, toIdList, data)
                else:
                    Logger.logDebug("MessageManager._onMessage", "Command not found:", command)

        except Exception as ex:
            Logger.logInfo(ex)
#end of _MessageManager

MessageManager = __MessageManager()