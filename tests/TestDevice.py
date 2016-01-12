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
		print "Test database:"+TEST_DB

	def test_init(self): # check if Device inits correct
		expected = False
		dev = Device()
		self.assertEqual(dev==None,expected)
		self.conn = sqlite3.connect(TEST_DB)
		pass

	def test_DeviceSetTask(self):
		#check if task set correctly
		expected = "1"
		dev = Device()
		dev.setStatus("1")

		self.assertEqual(dev.status, expected)

	def test_DeviceSave(self):
		expected = "Test01" # Expected device alias
		actual = ""

		dev = Device(alias="Test01")

		dev.save()

		conn = sqlite3.connect(TEST_DB)

		cur = conn.cursor()

		for row in cur.execute("select alias from Devices where alias='Test01'"):
			actual = row[0]

		wait(1)

		self.assertEqual(expected, actual)

		Database.query("delete from Devices where alias='Test01'")

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
