import sqlite3 as lite
import sys
con = None
try:
	#con = lite.connect('newtest.db')
    con = lite.connect('data/testdb.db')
    cur = con.cursor()
    #cur.execute('SELECT SQLITE_VERSION()')
    cur.execute('SELECT * from stuff')
    #data = cur.fetchone()
    #print (f'SQLite version: {data}')
    #cur.execute('SELECT SQLITE_VERSION()')
	#data = cur.fetchone()
	#print(f'SQLite version: {data}')

    data = cur.fetchall()

    for row in data :
        print(row)
    

except lite.Error as e :
	print (f"Error {e.args[0]}")
finally :
	if con:
		con.close()
