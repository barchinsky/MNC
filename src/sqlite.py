#!/usr/bin/env python

import sqlite3
from ConfigManager import ConfigManager

class Database:
	_cfm = ConfigManager()
	_host = ''
	_port = ''
	_user = ''
	_paswd = ''
	_location = _cfm.getDbLocation()
	_db = ''

	def __init__(self,isTest=False):

		self._db = ( self._cfm.getDb() , self._cfm.getTestDb() )[ isTest ]
		print 'Used database:'+self._db

		try:
			self._conn = sqlite3.connect(self._location+self._db) #connect to database
			self._conn.row_factory = self.dict_factory
			#print "%s database loaded"%(self._db)
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