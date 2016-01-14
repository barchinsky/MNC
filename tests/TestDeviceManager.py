#!/usr/bin/env python

import unittest
import sys
sys.path.append("..")
from src.DeviceManager import DeviceManager

class TestDeviceManager(unittest.TestCase):
	def test_test(self):
		self.assertEqual(1,1)

if __name__=="__main__":
	unittest.main()