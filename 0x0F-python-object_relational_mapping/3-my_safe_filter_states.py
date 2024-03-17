#!/usr/bin/python3
"""Safe version of 2-my_filter_states.py"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    n = cur.execute("SELECT * FROM states WHERE name=%s \
                    COLLATE utf8mb4_bin", (argv[4], ))
    for i in range(n):
        print(cur.fetchone())
