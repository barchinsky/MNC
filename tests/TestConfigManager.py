#!/usr/bin/env python

import unittest
import sys
sys.path.append('..')
from src.ConfigManager import ConfigManager

class TestConfigManager(unittest.TestCase):
	def test_ConfigManagerGetServerHost(self):
		cfm = ConfigManager()
		expected = '127.0.0.1'
		actual = cfm.getServerHost()
		self.assertEqual(expected, actual)

	def test_ConfigManagerGetServerPort(self):
		cfm = ConfigManager()
		expected = 9801
		actual = cfm.getServerPort()
		self.assertEqual(expected, actual)

	def test_ConfigManagerGetDbLocation(self):
		cfm = ConfigManager()
		expected = '/home/max/Dropbox/study/6th_course/diploma/MNC/db/'
		actual = cfm.getDbLocation()
		self.assertEqual(expected, actual)

	def test_ConfigManagerGetDb(self):
		cfm = ConfigManager()
		expected = 'mnc.db'
		actual = cfm.getDb()
		self.assertEqual(expected, actual)

	def test_ConfigManagerGetTestDb(self):
		cfm = ConfigManager()
		expected = 'test_mnc.db'
		actual = cfm.getTestDb()
		self.assertEqual(expected, actual)

if __name__ == "__main__":
	unittest.main()