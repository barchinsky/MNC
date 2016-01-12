#!/usr/bin/env python

''' This class will manage(add,remove,update,get all info) monitoring devices '''

from Device import Device
from sqlite import Database

class DeviceManager():
	_devices = []
	_db = Database()
	
	def __init__(self):
		pass

	# Load all devices from db
	def load(self):
		q = "select * from Devices"
		for device in self._db.query(q):
			dev = Device(id=device['id'], host=device['host'], port=device['port'], alias=device['alias'], location=device['location'], task=device['task'], status=device['status'], type=device['type'] )
			self._devices.append(dev)

		print self._devices

