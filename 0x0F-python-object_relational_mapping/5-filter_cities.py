#!/usr/bin/python3

""" Module that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    """function takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa"""

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    rows = curs.fetchall()
    print(", ".join([row[0] for row in rows]))
    curs.close()
    db.close()
