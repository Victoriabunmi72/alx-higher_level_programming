#!/usr/bin/python3
"""A script that install states from the database"""

import MySQLdb
import sys

username, password, dbname = sys.argv[1:]

conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname, charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
