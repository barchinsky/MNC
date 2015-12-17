#!/usr/bin/env python

try:
	import sys
	sys.path.append("..");

	import unittest
	from src.RequestProcessor import RequestProcessor
	import json
except Exception as e:
	print "TestRequestProcessor.py::Bad import."


class TestRequestProcessor(unittest.TestCase):

	def test_init(self):
		self.assertEqual('FOO', 'FOO')

	def test_buildResponse(self):
		expected =	{	u'header': { \
						u'type':"serverResp",\
						u'status':"success",\
						u'sourceName':"MNC",\
						u'sourceID': "MNC1" \
					},\
					u'payload': {\
						u'data': "Ok!" \
					}\
				
}
		rp = RequestProcessor()
		actual = rp.buildResponse(status="success",data="Ok!")

		self.assertEqual( actual, expected )

	def test_buildResponseDump(self):
		expected =	'{"header": {"status": "success", "sourceName": "MNC", "type": "serverResp", "sourceID": "MNC1"}, "payload": {"data": "Ok!"}}'

		rp = RequestProcessor()
		response = rp.buildResponse(status="success", data="Ok!")

		actual = json.dumps(response)

		self.assertEqual( actual, expected )



if __name__ == '__main__':
	unittest.main()