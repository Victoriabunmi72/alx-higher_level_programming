#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == "__main__":
    
    conn = MySQLdb.connect(host="localhost", port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8")

    """execute the query to retrieve information about the state."""
    cur = conn.cursor()
    cur.execute(query, (state_name,))
    query = " ".join([
            "SELECT * FROM states",
            "WHERE name LIKE BINARY '{}'",
            "ORDER BY id ASC",
            ]).format(sys.argv[4])

    """fetching and printing out the, result"""
    result = cur.fetchall()
    for row in result:
        print(row)

    """closing the cursor and connection"""
    cur.close()
    conn.close()
