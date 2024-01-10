#!/usr/bin/python3


'''
a script that returns a safely filtered list of all 
states based on name entered from the database
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    search_query = argv[4]
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
                ORDER BY id ASC",(search_query,))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()

