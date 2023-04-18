#!/usr/bin/python3

"""A script that lists all states"""

import MySQLdb
import sys

if __name__ == "__main__":

    username, password, dbname = sys.argv[1:]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname,
            charset="utf8")

    cur = db.cursor()

    myQuery = "".join[
            "SELECT * FROM states WHERE name LIKE BINARY 'N%'",
            "ORDER BY states.id ASC"]

    cur.execute(myQuery)
    curs = cur.fetchall()

    """print the state names, while iterating through the rows."""
    for row in curs:
        print(row)

cur.close()
db.close()
