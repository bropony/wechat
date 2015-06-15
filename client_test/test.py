"""
* @name test.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/15 19:16
*
* @desc test.py
"""
import sys
import os
cwd_dir = os.path.split(__file__)[0]
parent_dir = os.path.split(cwd_dir)[0]
sys.path.append(parent_dir)

from test.SerializerTest import runTest

if __name__ == '__main__':
    runTest()