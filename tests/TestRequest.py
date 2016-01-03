#!/usr/bin/env python

try:
	import sys
	sys.path.append("..");

	import unittest
	from src.Request import Request
	import json
except Exception as e:
	print "TestRequestProcessor.py::Bad import."

class TestRequest(unittest.TestCase):

	def __init__(self, *args, **kwargs):
 		super(TestRequest, self).__init__(*args, **kwargs)
 		self.prepare()

	def prepare(self):
		self._msg = '{\
					"header":{\
						"type":"test",\
						"sourceName":"test",\
						"sourceID":"test1"\
					},\
					"payload":{\
						"data":"Test"\
					}\
				}'

		self._rq = Request(self._msg)

	def test_init(self):
		self.assertEqual('FOO', 'FOO')

	def test_createResponseValid(self):
		rq = Request(self._msg)

		self.assertEqual(self._rq.isValid, True)

	def test_createResponseInvalid(self):
		''' Create request with empty input msg.
		Expected: Failed with error.
		Error: No JSON object could be decoded
		'''

		rq = Request()

		self.assertEqual(rq.isValid, False)

	def test_RequestTypeProp(self):
		''' Check if type property loaded successfully '''

		self.assertEqual(self._rq.type,'test')

	def test_RequestSourceIDProp(self):
		''' Check if sourceID property loaded successfully '''

		self.assertEqual(self._rq.sourceID,'test1')

	def test_RequestSourceNameProp(self):
		''' Check if sourceName property loaded successfully '''

		self.assertEqual(self._rq.sourceName,'test')

	def test_RequestpayloadProp(self):
		''' Check if data property loaded successfully '''

		self.assertEqual(self._rq.data,'Test')


if __name__ == '__main__':
	unittest.main()
