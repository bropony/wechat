#
# file: main_db.py
#
# author: ahda86@gmail.com
#
# CAUTION: This file is Auto-Generated.
# Please DON'T modify this file EVEN if you know what you are doing.
#


import datetime
from gamit.message.message import MessageBlock
import message.gate.gatemsg


class AnRmiTest:
    def __init__(self):
        self.message = message.gate.gatemsg.SMessage()
        self.ip = str()
        self.shortDesc = str()

    def _read(self, _is):
        self.message._read(_is)
        self.ip = _is.readString()
        self.shortDesc = _is.readString()

    def _write(self, _os):
        print("Write AnRmiTest Out")
        self.message._write(_os)
        _os.writeString(self.ip)
        _os.writeString(self.shortDesc)

    def _fromJson(self, js):
        if 'message' in js and isinstance(js['message'], message.gate.gatemsg.SMessage):
            self.message._fromJson(js['message'])
        if 'ip' in js and isinstance(js['ip'], str):
            self.ip = js['ip']
        if 'shortDesc' in js and isinstance(js['shortDesc'], str):
            self.shortDesc = js['shortDesc']

    def _toJson(self):
        js = dict()
        js['message'] = self.message._toJson()
        js['ip'] = self.ip
        js['shortDesc'] = self.shortDesc
        return js

MessageBlock.register(AnRmiTest)

