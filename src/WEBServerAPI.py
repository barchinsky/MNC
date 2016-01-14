#!usr/bin/env python

'''
API for managing devices
'''

from flask import Flask
import json
import sys
sys.path.append('..')
from templates.template import RESPONSE_V2
from templates.template import HELP
from utils.WebAPIUtils import buildResponse

app = Flask(__name__)

@app.route('/')
def index():
	return buildResponse(status="1",data='"MNC Web server API v.0.1"')

@app.route('/help')
def help():
	return buildResponse(status="1",data=HELP)

@app.route('/mnc/')
def mnc():
	return buildResponse(status="1",data=HELP)

@app.route('/mnc/api')
def api():
	return buildResponse(status="1",data=HELP)

# Return list of all devices
@app.route('/mnc/api/v0.1/getDevices')
def getDevices():
	data = [{"1":0},{"2":1},{"3":2}]
	return buildResponse( status="1", data=json.dumps(data) )




if __name__ == '__main__':
	app.run(debug=True)