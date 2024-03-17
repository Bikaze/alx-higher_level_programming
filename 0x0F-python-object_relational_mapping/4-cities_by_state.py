#!/usr/bin/python3
"""The following code lists all rows in the cities table joined with
states table"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    n = cur.execute("SELECT cities.id, cities.name, states.name FROM\
                    cities JOIN states ON state_id=states.id")
    for i in range(n):
        print(cur.fetchone())
