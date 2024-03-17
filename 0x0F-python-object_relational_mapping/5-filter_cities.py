#!/usr/bin/python3
"""The following code lists all rows in the cities table joined with
states table"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    n = cur.execute(f"SELECT cities.name FROM\
                    cities JOIN states ON state_id=states.id WHERE\
                    states.name=%s", (argv[4],))
    b = 0
    for i in cur.fetchall():
        for a in i:
            b += 1
            if b == 1:
                print(a, end="")
            else:
                print(",",  a, end="")
    print()
