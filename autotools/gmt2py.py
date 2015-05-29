"""
* @name gmt2py
*
* @author ahda86@gmail.com
*
* @date 2015/5/29 14:36
*
* @desc gmt2py
"""
import sys
from optparse import OptionParser
from autotools.gmtloader.structmanager import StructManager

class Gmt2Py:
    def __init__(self, manger, loader):
        self.structManager = manger
        self.loader = loader

    def generate(self):
        print("Generation Python code of {}".format(self.loader.filepath))

def main():
    parser = OptionParser()
    parser.add_option("-n", "--namespace", help="root python module name",
                      dest="scope")
    parser.add_option("-g", "--gmt-dir", help="root directory of gmt files",
                      dest="inRootDir")
    parser.add_option("-o", "--out-dir", help="root directory of generated python files",
                      dest="outRootDir")
    parser.add_option("-f", "--file", dest="sources", action="append",
                      help="relative path of source gmt file. Multi-assignation is allowed.")
    #parser.add_option("-h","--help", help="show this message", action="store_false")

    options, args = parser.parse_args()

    if len(sys.argv) < 2 or options.help:
        parser.print_help()
        return

    scope = options.scope or ""
    inRootDir = options.inRootDir or "."
    outRootDir = options.outRootDir or "."
    files = options.files or []

    if not files:
        return

    structManager = StructManager(scope, inRootDir, outRootDir)
    loaders = []
    for f in files:
        loader = structManager.loadFile(f)
        gmt = Gmt2Py(structManager, loader)
        gmt.generate()

if __name__ == "__main__":
    main()
