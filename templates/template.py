#!/usr/bin/env python

RESPONSE = "{u'header': {u'type': '$rtype',u'status': '$status',u'sourceName': '$sourceName',u'sourceID': '$sourceID'},u'payload': {u'data': '$data'}}"
TEST_REQUEST = '{"header": {"type": "test","sourceName": "test","sourceID": "test1"},"payload": {"data": "Test"}}'
HELP='[ {"path": "/help","description": "Display server API"}]'
RESPONSE_V2 = '{"header": {"type": "%s","status": "%s","sourceName": "%s","sourceID": "%s"},"payload": {"data": %s}}'