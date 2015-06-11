"""
* @name manager.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/11 14:50
*
* @desc manager.py
"""

from staticdata.loader.loader import load
import abc

class ManagerBase(metaclass=abc.ABCMeta):
    def __call__(self, *args, **kwargs):
        return self

    def __init__(self, loader):
        self.data = []
        self.loader = loader

    def loadConfig(self, filepath):
        self.data = load(filepath, self.loader)
# end of ManagerBase
