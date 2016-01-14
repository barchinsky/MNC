#!/usr/bin/env python

import sqlite3
import sys
sys.path.append("..")
from src.ConfigManager import ConfigManager

def initDb():
	conn = sqlite3.connect( ConfigManager().getDbLocation()+ConfigManager().getTestDb() )
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
	conn = sqlite3.connect(ConfigManager().getDbLocation()+ConfigManager().getTestDb())
	c = conn.cursor()

	# data to be inserted
	data = [('"localhost"',9901,'"TD01"','"10.21;13.45"','"New"','"G"'),
		('"134.22.43.43"',10001,'"TD02"','"15.0;45.85"','"New"','"G"')]

	# Insert mock data reques
	req = '''INSERT INTO Devices(host,port,alias,location,status,type) VALUES(?,?,?,?,?,?)'''
	
	c.executemany(req,data)

	conn.commit()

def selectDevices():
	conn = sqlite3.connect(ConfigManager().getDbLocation()+ConfigManager().getTestDb())
	c = conn.cursor()

	for row in c.execute("select host,port,alias from Devices"):
		print row[0],row[1],row[2]

if __name__ == "__main__":
	#initDb()
	#loadTestInfo()
	selectDevices()