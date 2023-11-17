#!/usr/bin/python3

""" Module that t lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    """function that lists all states from the database hbtn_0e_0_usa"""

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
