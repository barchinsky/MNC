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
	from templates.template import RESPONSE #load msg templates
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
			response = self.buildResponse( status="failed", data="Wrong request format." )
		else:
			response = self.parse(self._request)

		return json.dumps(response)

	def parse(self, request):
		''' Parse incoming request '''

		response = ""
		
		if request.type == "test":
			print "Test request goted."
			response = self.startTest(request)
		else:
			response = self.buildResponse( status="failed", data="Wrong request type." )

		return response

	def startTest(self,request):
		''' Test request handler '''

		sourceID = request.sourceID

		if self.isExistingSourceID(sourceID):
			response = self.buildResponse("success","Ok!")

		return response

	def isExistingSourceID(self,sourceID):
		'''
		Check if such object exists in DB
		Returns True or False
		'''

		print "isExistingSourceID(self,sourceID)"

		if sourceID == "test1":
			return True
		else:
			print "Wrong sourceID:%s"%(sourceID)
			return False

	def buildResponse(self, _status,_data, _rtype="serverResp",_sourceName="MNC", _sourceID="MNC1"):
		''' 
		Build server response using given params 
		Returns response in string type
		'''

		response = Template(RESPONSE) #load template
		args = dict(rtype=_rtype, status=_status, sourceName=_sourceName, sourceID=_sourceID, data=_data) # prepare template args

		response = response.safe_substitute(args).replace("\t","")

		return response



