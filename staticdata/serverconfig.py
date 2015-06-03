"""
* @name serverconfig.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/3 15:14
*
* @desc serverconfig.py
"""

import xml.etree.ElementTree as xmlParser
import os.path
import sys

class Channel:
    def __init__(self, type, id, ip, port):
        self.type = type
        self.id = id
        self.ip = ip
        self.port = port

class __ServerConfig:
    def __init__(self):
        self.publicIp = ""
        self.privateIp = ""
        self.db1Ip = ""
        self.db2Ip = ""
        self.portVar = ""
        self.dbVer = ""
        self.isDebug = False

        self.channels = {}

    def loadConfig(self):
        cwd = os.path.split(__file__)[0]
        serverConfig = os.path.join(cwd, "../config/server_config.xml")
        channelConfig = os.path.join(cwd, "../config/channel.xml")

        serverTree = xmlParser.parse(serverConfig)
        root = serverTree.getroot()
        for child in root:
            tag = child.tag
            text = child.text or ""
            if tag == "public_ip":
                self.publicIp = text
            elif tag == "private_ip":
                self.privateIp = text
            elif tag == "db_ip1":
                self.db1Ip = text
            elif tag == "db_ip2":
                self.db2Ip = text
            elif tag == "port_var":
                self.portVar = text
            elif tag == "db_ver":
                self.dbVer = text
            elif tag == "is_debug":
                self.isDebug = False if text == "False" else True

        channelTree = xmlParser.parse(channelConfig)
        root = channelTree.getroot()
        for child in root:
            tag = child.tag
            attrib = child.attrib
            channelType = int(attrib["type"])
            channelId = int(attrib["id"])
            channelIp = attrib["ip"]
            chnanelPort = attrib["port"]
            chnanelPort = chnanelPort.replace("var", self.portVar)

            channel = Channel(channelType, channelId, channelIp, chnanelPort)
            self.channels[channelId] = channel

    def getChannelByType(self, channelType):
        for _, channel in self.channels.items():
            if channel.type == channelType:
                return channel
        return None

    def getChannelById(self, channelId):
        if channelId in self.channels:
            return self.channels[channelId]
        return None

ServerConfigManager = __ServerConfig()

if __name__ == "__main__":
    ServerConfigManager.loadConfig()