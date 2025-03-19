#!/usr/bin/python3
"""
Modulo comment
"""


import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        user = username,
        passwd = password,
        db = db_name,
        port = 3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
