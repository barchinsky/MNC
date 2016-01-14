#!/usr/bin/env python

try:
	import unittest
	import sys
	sys.path.append('..')
	from src.Device import Device
	from src.ConfigManager import ConfigManager
	from src.sqlite import Database
	import json
	import sqlite3
	import time
except Exception as e:
	print "TestDevice.py::Bad import.%s"%(e)

TEST_DB = ConfigManager().getDbLocation()+ConfigManager().getTestDb()

class TestDevice(unittest.TestCase):
	def __init__(self,*args,**kwargs):
		super(TestDevice, self).__init__(*args,**kwargs)
		#print "Test database:"+TEST_DB

	def test_init(self): # check if Device inits correct
		expected = False
		dev = Device()
		self.assertEqual(dev==None,expected)
		pass

	def test_DeviceSetTask(self):
		#check if task set correctly
		expected = "1"
		dev = Device()
		dev.setStatus("1")

		self.assertEqual(dev.status, expected)

	def test_DeviceSave(self):
		expected = 1 # Expected device alias
		actual = ""

		db = Database(isTest=True)

		res = db.query("select alias from Devices where alias='Test01'")
		
		if ( len(res) ):
			print "Database is not clear. Test Can't be started."
			self.assertEqual( 0, len(res) ) # check if database is clear

		dev = Device(alias="Test01")

		dev.save(isTest=True)

		wait(1)

		res = db.query("select count(*) as num from Devices where alias='Test01'")
		actual = res[0]['num']

		self.assertEqual(expected, actual)

		db.query("delete from Devices where alias='Test01'")

	def test_DeviceWithoutLocation(self):
		expected = {'lat':'-1','lon':'-1'}

		dev = Device()

		actual = dev.location

		self.assertEqual(expected, actual)


def wait(interval):
	end_time = time.time()+interval
	while end_time > time.time():
		continue

if __name__=="__main__":
	unittest.main()
