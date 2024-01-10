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
    cur.execute("SELECT cities.name FROM cities INNER JOIN \
                states ON cities.state_id = states.id WHERE \
                states.name LIKE BINARY %s \
                ORDER BY cities.id ASC",(search_query,))
    cities = cur.fetchall()
    my_list = []
    for city in cities:
        my_list.append(city[0])
    print(", ".join(my_list))        
    cur.close()
    db.close()

