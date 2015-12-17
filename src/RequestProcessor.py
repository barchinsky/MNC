#!/usr/bin/env python

'''

This module developed to process incoming request to the server.

'''

try:
	import json
except NameError as e:
	print "Import error:%s"%(e)

class RequestProcessor():
	def __init__(self):
		pass

	def process(self,msg):
		''' This method will parse request and route it to appropriate handler. '''

		print "RequestProcessor.process:%s"%(msg)

		try:
			jsnMsg = json.loads(msg)
		except Exception as e:
			print e
			response = self.buildResponse(status="failed",data="Bad request format.")
			return json.dumps(response)

		header = jsnMsg["header"]
		data = jsnMsg["payload"]

		if header["type"] == "test":
			response = self.startTest(header)
		else:
			response = self.buildResponse(status="failed", data="Wrong request type.")

		return json.dumps(response)

	def startTest(self,header):
		sourceID = header["sourceID"]

		if self.isExistingSourceID(sourceID):
			response = self.buildResponse("success","Ok!")

		return response

	def isExistingSourceID(self,sourceID):
		'''
		TODO: implement id verificaton.
		'''

		print "isExistingSourceID(self,sourceID)"

		print "Just a mock function. Nothing will happend."

		if sourceID == "test1":
			return True
		else:
			print "Wrong sourceID:%s"%(sourceID)
			return False

	def buildResponse(self, status,data, rtype="serverResp",sourceName="MNC", sourceID="MNC1"):
		response = 	{	u'header': { \
						u'type':rtype,\
						u'status':status,\
						u'sourceName':sourceName,\
						u'sourceID': sourceID \
					},\
					u'payload': {\
						u'data': data \
					}\
				}
		return response



