"""
* @name SerializerTest.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/15 18:03
*
* @desc SerializerTest.py
"""

from message.gate.gatemsg import *
from message.db.main_db import *
from gamit.serialize.serializer import Serializer

def printObj(obj, desc):
    print("[{}] {}:".format(desc, obj.__class__.__name__))

    if isinstance(obj, list):
        for i in range(len(obj)):
            printObj(obj[i], "[{}.{}]".format(desc, i))
    elif isinstance(obj, dict):
        for k in obj:
            printObj(obj[k], "[{}.{}]".format(desc, k))
    else:
        for key in obj.__slots__:
            print("\t{}: {}".format(key, obj[key]))


def runTest():
    msg = SMessage()
    msg.var6 = "what"
    msg.var7 = datetime.datetime.strptime("2011-01-01 11:11:11", "%Y-%m-%d %H:%M:%S")
    for i in range(10):
        msg.intList.append(i)
        msg.dictStrInt[str(i)] = i

    dictMsg = DictMessage()
    dictMsg[1] = msg
    dictMsg[2] = msg

    printObj(dictMsg, "SRC")

    os = Serializer()
    os.startToWrite()
    dictMsg._write(os)

    _is = Serializer(os.getBuffer())
    _is.startToRead()
    backDicMsg = DictMessage()
    backDicMsg._read(_is)
    printObj(backDicMsg, "BACK")

    js = dictMsg._toJson()
    jsBack = DictMessage()
    jsBack._fromJson(js)

    printObj(jsBack, "JSSS")