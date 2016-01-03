#!/usr/bin/env python

import sys
sys.path.append("..")

try:
	import socket
	import ConfigParser
	import json
	from template.template import TEST_REQUEST
except Exception as e:
	print "Import error: %s"%(e)


class MockClient():
	def __init__(self):
		self.config = ConfigParser.RawConfigParser()
		self.config.read("../conf/config.cfg")
		self.host = self.config.get("server","host")
		self.port = self.config.getint("server","port")

		# Create a TCP/IP socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def start(self):
		# Connect the socket to the port where the server is listening
		serverAddress = (self.host, self.port)
		print 'connecting to %s port %s' % serverAddress
		self.sock.connect(serverAddress)

		try:
			
			# Send data
			message = TEST_REQUEST

			print 'sending "%s"' % message
			self.sock.sendall(message)

			# Look for the response
			buf = self.sock.recv(1000)

			data = json.loads(buf);

			print "Response received:%s"%( data )

		finally:
			print 'closing socket'
			self.sock.close()

if __name__ == "__main__":
	client = MockClient()
	client.start()