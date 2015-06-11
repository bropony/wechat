"""
* @name db2gmt.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/10 20:03
*
* @desc db2gmt.py
"""

from optparse import OptionParser
import sys
import os
import re
import MySQLdb

import gmt2py

def toCamel(src, cap):
    tags = re.split(r'_', src)
    flag = 0 if cap else 1

    tags[flag:] = [t.capitalize() for t in tags[flag:]]
    return "".join(tags)

def table2gmt(name, fields, gmtOutDir, pyOutDir):
    if not os.path.exists(gmtOutDir):
        os.makedirs(gmtOutDir)

    tableName = toCamel(name, True)
    outpath = os.path.join(gmtOutDir, tableName + ".gmt")
    fout = open(outpath, "w")
    fout.write("#\n# This File Is Auto-Generated. Please DON'T Modify It.\n#\n")
    fout.write("struct {}:\n".format(tableName))
    for field in fields:
        name = toCamel(field[0], False)
        gmtType = "xxx"
        dbType = field[1]
        if dbType.startswith("int"):
            gmtType = "int"
            m = re.search(r"(\d+)", dbType)
            if m:
                val = int(m.group(1))
                if val > 11:
                    gmtType = "long"
        elif dbType.startswith("varchar") or dbType.startswith("char"):
            gmtType = "string"
        elif dbType.startswith("float"):
            gmtType = "float"
            m = re.search(r"(\d+)", dbType)
            if m:
                val = int(m.group(1))
                if val > 11:
                    gmtType = "double"
        elif dbType.startswith("date"):
            gmtType = "date"

        fout.write("    {} {}\n".format(gmtType, name))

    fout.write("\n")
    fout.write("list<{0}> Seq{0}".format(tableName))
    fout.close()

    if not pyOutDir:
        return

    if not os.path.exists(pyOutDir):
        os.makedirs(pyOutDir)

    argv = []
    argv.append(gmt2py.__name__)
    argv.append("-g" + gmtOutDir)
    argv.append("-o" + pyOutDir)
    argv.append("-f" + tableName + ".gmt")
    sys.argv = argv
    gmt2py.main()

def main():
    parser = OptionParser()
    parser.add_option("-H", "--host", help="database host. Default:localhost",
                      dest="host")
    parser.add_option("-P", "--port", help="port of database host. Default: 3306",
                      dest="port", type="int")
    parser.add_option("-d", "--database", help="database. Always required", dest="database")
    parser.add_option("-u", "--user", help="username. Default: root", dest="username")
    parser.add_option("-p", "--passwd", help="passwords. Always required", dest="passwd")
    parser.add_option("-g", "--gmt-out-dir", dest="gmtOutDir",
                      help="output dir of generated gmt files. Default: working dir")
    parser.add_option("-c", "--py-code-out-dir", dest="pyOutDir",
                      help="output dir of generated py files. If not given, no py files will be generated.")
    parser.add_option("-t", "--table", dest="tables", action="append",
                      help="Table to deal with. By default, all tables are dealt with. "
                           "Multi-assignation is allowed.")

    options, args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return

    host = options.host or "localhost"
    port = options.port or 3306
    database = options.database or ""
    username = options.username or "root"
    passwd = options.passwd or ""
    gmtOutDir = options.gmtOutDir or "."
    tables = options.tables or []
    pyOutDir = options.pyOutDir or ""

    if not database:
        print("database is not specified")
        sys.exit()

    conn = MySQLdb.connect(host=host, user=username, passwd=passwd, db=database, port=port)
    cursor = conn.cursor()

    cursor.execute("show tables")
    __tables = []
    for t in cursor.fetchall():
        __tables.append(t[0])

    if not tables:
        tables = __tables
    else:
        for t in tables:
            if t not in __tables:
                print("table {} is not found.".format(t))
                sys.exit()

    print("Starting jobs")
    for t in tables:
        cursor.execute("desc {}".format(t))
        fields = cursor.fetchall()
        print("Dealing with '{}'".format(t))
        table2gmt(t, fields, gmtOutDir, pyOutDir)
    print("All jobs done...")

if __name__ == "__main__":
    main()