#!/usr/bin/env python

import unittest
import sys
sys.path.append("..")
from utils.WebAPIUtils import *
from templates.template import HELP
import json

class TestWebAPIUtils(unittest.TestCase):
	def test_buildResponseWithDataIsString(self):
		'''
			def buildResponse(status,data, rtype="serverResp",sourceName="MNC", sourceID="MNC1")
		'''
		data='["Test"]'
		expected = '{"header": {"type": "serverResp","status": "1","sourceName": "MNC","sourceID": "MNC1"},"payload": {"data": ["Test"]}}'
		actual = buildResponse(status="1",data=data)
		self.assertEqual(expected,actual)

	def test_buildResponseMessageIsValidJSON(self):
		data=HELP
		actual = buildResponse(status="1",data=data)

		jsformat=json.loads(actual)
		self.assertEqual("1",jsformat["header"]["status"])


if __name__=="__main__":
	unittest.main()