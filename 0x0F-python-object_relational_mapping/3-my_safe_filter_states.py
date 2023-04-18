#!/usr/bin/python3

"""SQL injection"""

import MySQLdb
import sys

if __name__ == ("__main__"):

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")

    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE %s", (sys.argv[4], ))

    # HERE I have to know SQL to grab all states in my database

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
