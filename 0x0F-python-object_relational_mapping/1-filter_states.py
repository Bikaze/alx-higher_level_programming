#!/usr/bin/python3
"""The following code lists rows in the 'states' database
with name starting with 'N'"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    n = cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    for i in range(n):
        print(cur.fetchone())
