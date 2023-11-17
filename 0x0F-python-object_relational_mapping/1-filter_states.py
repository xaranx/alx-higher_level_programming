#!/usr/bin/python3

""" Module that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    """function that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\ ORDER BY id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
