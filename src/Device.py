#!/usr/bin/env python

'''
	This class implements base structure for monitoring device.
'''
from sqlite import Database

class Device:
	def __init__(self,alias="", host="", port=0, location = {'lat':'-1','lon':'-1'}, type="", task="", status=""):
		self._id = -1
		self._host = host
		self._port = port
		self._alias = alias
		self._location = location
		self._type = type # Ground | Fly
		self._task = task
		self._status = status # New | Registered | Active | Unreachable | Lost
		self._saved = False
		self._db = Database()

	def save(self):
		'''
		Save device to db
		'''

		query = '''INSERT INTO Devices(host, port, alias, location, type, task, status) VALUES(\
				%s,\
				%d,\
				%s,\
				%s,\
				%s,\
				%s,\
				%s)'''%('"%s"'%(self._host), self._port, '"%s"'%(self._alias), '"(%s;%s)"'%( self._location['lat'], self._location['lon'] ), '"%s"'%(self._type), '"%s"'%(self._task), '"%s"'%(self._status) )
	
		try:
			res = self._db.query(query)
			#print 'Device::save() res:%s'%(res)
		except Exception as e:
			print "Device().save(): Insert error: %s"%(e)
		
	def register(self):
		pass

	def setTask(self,task):
		self._task = task

	def updateType(self,newType):
		self._type = newType


	def setStatus(self,newStatus):
		self._status = newStatus

	def updateLocation(self,newLocation):
		self._location = newLocation

	def __str__(self):
		return "%d,%s,%d,%s,%s,%s,%s"%(self._id, self._host, self._port, self._alias, '(%s;%s)'%(self._location['lat'], self._location['lon']), self._type, self._task, self._status)

	@property
	def id(self):
		return self._id

	@property
	def alias(self):
		return self._alias

	@property
	def location(self):
		return self._location

	@property
	def type(self):
		return self._type
	
	@property
	def status(self):
		return self._status