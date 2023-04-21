#!/usr/bin/python3
"""argument and lists all cities of that state,
using the database hbtn_0e_4_usa"""

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
    myQuery = " ".join([
        "SELECT cities.name FROM cities",
        "INNER JOIN states ON states.id=cities.state_id",
        "WHERE states.name LIKE BINARY '{}'",
        "ORDER BY cities.id",
        ]).format(sys.argv[4])
    cur.execute(myQuery)
    res = cur.fetchall()
    strRes = ','.join([i[0] for i in res])
    print(strRes)
    cur.close()
    conn.close()
