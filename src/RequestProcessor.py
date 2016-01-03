#!/usr/bin/env python

'''

This module developed to process incoming request to the server.

'''

import sys
sys.path.append('..')

import json
from string import Template

try:
	from Request import Request
	from template.template import RESPONSE #load msg templates
except NameError as e:
	print "Import error:%s"%(e)

class RequestProcessor():
	def __init__(self):
		self._request = None

	def process(self,msg):
		''' This method will parse request and route it to appropriate handler. '''

		print "RequestProcessor.process:%s"%(msg)

		self._request = Request(msg)

		if not self._request.isValid:
			response = self.buildResponse( status="failed", data="Wrong request type." )
		else:
			response = self.parse(self._request)

		return json.dumps(response)

	def parse(self, request):
		''' Parse incoming request '''

		response = ""
		
		if request.type == "test":
			print "Test request goted."
			response = self.buildResponse("success","Data successfully received")

		return response

	def startTest(self,header):
		''' Test request handler '''

		sourceID = header["sourceID"]

		if self.isExistingSourceID(sourceID):
			response = self.buildResponse("success","Ok!")

		return response

	def isExistingSourceID(self,sourceID):
		'''
		TODO: implement id verificaton.
		'''

		print "isExistingSourceID(self,sourceID)"

		if sourceID == "test1":
			return True
		else:
			print "Wrong sourceID:%s"%(sourceID)
			return False

	def buildResponse(self, _status,_data, _rtype="serverResp",_sourceName="MNC", _sourceID="MNC1"):

		response = Template(RESPONSE)
		args = dict(rtype=_rtype, status=_status, sourceName=_sourceName, sourceID=_sourceID, data=_data)

		response = response.safe_substitute(args).replace("\t","")
		return response



