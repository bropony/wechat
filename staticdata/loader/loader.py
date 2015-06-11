"""
* @name loader
*
* @author ahda86@gmail.com
*
* @date 2015/6/11 14:44
*
* @desc loader
"""

import json

def load(jsFile, loader):
    fjs = open(jsFile)
    js = json.load(fjs)
    fjs.close()

    res = loader(js)

    return js
