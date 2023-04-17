#!/usr/bin/python3

"""A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":

    username, password, dbname = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                        passwd=password, db=dbname, charset="utf8")
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
                        # HERE I have to know SQL to grab all states in my database
    
    #print the state names, while iterating through the rows.
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
