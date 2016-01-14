#!/usr/bin/env python

import sys
sys.path.append("..")

try:
	import socket
	import json
	from templates.template import TEST_REQUEST
	from src.ConfigManager import ConfigManager
except Exception as e:
	print "mockClient.py Import error: %s"%(e)


class MockClient():
	def __init__(self):
		self._config =ConfigManager()
		self._host = self._config.getServerHost()
		self._port = self._config.getServerPort()

		# Create a TCP/IP socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def start(self):
		# Connect the socket to the port where the server is listening
		serverAddress = (self._host, self._port)
		print 'connecting to %s port %s' % serverAddress
		self.sock.connect(serverAddress)

		try:
			
			# Send data
			message = TEST_REQUEST

			print 'sending "%s"' % message
			self.sock.sendall(message)

			# Look for the response
			buf = self.sock.recv(1000)
			print "Response received:%s"%( buf )

			data = json.loads(buf);

		finally:
			print 'closing socket'
			self.sock.close()

if __name__ == "__main__":
	client = MockClient()
	client.start()