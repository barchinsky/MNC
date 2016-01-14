#!/usr/bin/env

'''

Server.py

Interface developed for listening incoming requests from monitoring modules.

'''

try:
	import socket
	from ConfigManager import ConfigManager
	from RequestProcessor import *
	import SocketServer
except NameError as e:
	print "Import error:%s"%(e)

class TCPReqHandler(SocketServer.BaseRequestHandler):
	"""
	The RequestHandler class for our server.

	It is instantiated once per connection to the server, and must
	override the handle() method to implement communication to the
	client.
	"""

	def handle(self):
		# self.request is the TCP socket connected to the client
		data = self.request.recv(1024).strip()
		print "{} wrote:".format(self.client_address[0])
		print data
		# just send back the same data, but upper-cased
		if data:
			print "Data received:%s from %s"%(data, self.client_address[0])

		response = RequestProcessor().process(data)
		
		self.request.sendall(response)

class Server():
	def __init__(self):
		self.cfm = ConfigManager()
		self._requestProcessor = RequestProcessor()

		self.host = self.cfm.getServerHost()
		self.port = self.cfm.getServerPort()
		self.addr = (self.host, self.port)

		self.server = SocketServer.TCPServer((self.host, self.port), TCPReqHandler)

	def start(self):
		''' Start listening serving '''
		print "Server stated on %s:%d"%(self.host, self.port)
		self.server.serve_forever()

