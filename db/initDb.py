#!/usr/bin/env python

import sqlite3

def initDb():
	conn = sqlite3.connect('mnc.db')
	c = conn.cursor()

	# Create  Tasks table
	c.execute('''CREATE TABLE Tasks
		(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			alias text,
			location text,
			task int,
			type text,
			description text
		)''')

	# Create  Devices table
	c.execute('''CREATE TABLE Devices
		(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			host text,
			port int,
			alias text,
			location text,
			task int,
			status text,
			type text,
			FOREIGN KEY(task) REFERENCES Tasks(id)
		)''')


	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()

def loadTestInfo():
	conn = sqlite3.connect('mnc.db')
	c = conn.cursor()

	# Insert mock data
	req = '''INSERT INTO Devices(host,port,alias,location,status,type) VALUES(\
			%s,\
			%d,\
			%s,\
			%s,\
			%s,\
			%s\
		)
		'''%('"localhost"',9901,'"TD01"','"10.21,13.45"','"New"','"G"')
	
	c.execute(req.replace("\t",""))

	conn.commit()

def selectDevices():
	conn = sqlite3.connect('mnc.db')
	c = conn.cursor()

	for row in c.execute("select host,port,alias from Devices"):
		print row[0],row[1],row[2]

if __name__ == "__main__":
	#initDb()
	#loadTestInfo()
	selectDevices()