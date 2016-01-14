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
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
	"admin": "admin",
}

@auth.get_password
def get_pw(username):
	if username in users:
		return users.get(username)
	return None

@app.route('/')
@auth.login_required
def index():
	return buildResponse(status="1",data='"MNC Web server API v.0.1"')

@app.route('/help')
@auth.login_required
def help():
	return buildResponse(status="1",data=HELP)

@app.route('/mnc/')
@auth.login_required
def mnc():
	return buildResponse(status="1",data=HELP)

@app.route('/mnc/api')
@auth.login_required
def api():
	return buildResponse(status="1",data=HELP)

# Return list of all devices
@app.route('/mnc/api/v0.1/getDevices')
@auth.login_required
def getDevices():
	data = [{"1":0},{"2":1},{"3":2}]
	return buildResponse( status="1", data=json.dumps(data) )




if __name__ == '__main__':
	app.run(debug=True)