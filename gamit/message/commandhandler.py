__author__ = 'mahanzhou'

import abc

class CommandHandlerBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def onMessage(self, command, toIdList, data):
        pass

