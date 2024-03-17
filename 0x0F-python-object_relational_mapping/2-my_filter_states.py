#!/usr/bin/python3
"""The following code lists rows in the 'states' database
with name being the fourth passed argument"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    n = cur.execute(f"SELECT * FROM states WHERE name='{argv[4]}'")
    for i in range(n):
        print(cur.fetchone())
