"""
* @name gate.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/3 10:26
*
* @desc gate.py
"""

import sys
import os.path

# add parent dir to searching paths
absPath = os.path.abspath(sys.argv[0])
absPath, _ = os.path.split(absPath)
absPath, _ = os.path.split(absPath)
sys.path.append(absPath)

def main():
    pass

if __name__ == "__main__":
    main()