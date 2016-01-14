#!/usr/bin/env python

'''
	Help utils for WEB server API
'''

import sys
sys.path.append("..")

from templates.template import RESPONSE_V2

def buildResponse(status,data, rtype="serverResp",sourceName="MNC", sourceID="MNC1"):
	'''
		RESPONSEV2 = "{u'header': {u'type': '%s',u'status': '%s',u'sourceName': '%s',u'sourceID': '%s'},u'payload': {u'data': '%s'}}"
	'''
	return RESPONSE_V2%(rtype,status,sourceName,sourceID,data)