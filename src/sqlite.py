#!/usr/bin/env python

import sqlite3
from ConfigManager import ConfigManager

class Database:
	_cfm = ConfigManager()
	_host = ''
	_port = ''
	_db = _cfm.getDbLocation()+_cfm.getDb()
	_user = ''
	_paswd = ''

	def __init__(self):
		try:
			self._conn = sqlite3.connect(self._db) #connect to database
			self._conn.row_factory = self.dict_factory
			#print "Database loaded"
		except Exception as e:
			print "Database import error: %s"%(e)

	def query(self,q): # perform query
		print "Database::query() q:%s"%(q)

		cur = self._conn.cursor()
		res = []

		for row in cur.execute(q):
			res.append(row)

		self._conn.commit() # commit changes if needed

		return res

	def dict_factory(sefl,cursor, row): # make dict instead of list 
		'''	
			result is dict
			key:  col description
			value: row element
		'''
		d = {}
		for idx, col in enumerate(cursor.description): # for each element of row description
			d[ col[0] ] = row[idx] # make a dictionary with appropriate row element

		return d

	def __del__(self):
		self._conn.close()