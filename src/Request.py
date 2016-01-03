#!/usr/bin/env python

try:
	import json
except Exception as e:
	print "Request.py: Import error: %s"%(e)

class Request:

	def __init__(self, msg=""):
		''' Define base prop '''

		self._body = {}
		self._header = {}
		self._payload = {}

		self._type = ""
		#self._status = ""
		self._sourceName = ""
		self._sourceID = ""
		self._payload = ""

		self._isValid = True

		self._load(msg)

	def _load(self, msg):
		''' Load request from json msg '''
		print "Request._load()"

		try: 
			jsnMsg = json.loads(msg)
		except Exception as e: # return if json is not valid
			print e
			self._isValid = False
			return
			#return json.dumps(response)

		self._header = jsnMsg["header"]
		self._type = self._header["type"]
		#self._status = self._header["status"]
		self._sourceName = self._header["sourceName"]
		self._sourceID = self._header["sourceID"]

		self._payload = jsnMsg["payload"]
		self._data = self._payload["data"]

		print "~Request._load()"

	@property
	def isValid(self):
		return self._isValid

	@property
	def type(self):
	    return self._type

	@property
	def sourceName(self):
	    return self._sourceName

	@property
	def sourceID(self):
	    return self._sourceID

	@property
	def payload(self):
	    return self._payload

	@property
	def data(self):
	    return self._data
	
	
	
	
	
	
	
