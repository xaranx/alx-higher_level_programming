#!/usr/bin/python3

""" Module that  takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument """

import sys
import MySQLdb

if __name__ == "__main__":
    """function that  takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument"""

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                 (sys.argv[4],))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
