#!/usr/bin/env

'''

Server.py

Interface developed for listening incoming requests from monitoring modules.

'''

try:
	import socket
	import ConfigParser
	from RequestProcessor import *
except NameError as e:
	print "Import error:%s"%(e)

class Server():
	def __init__(self):
		self.config = ConfigParser.RawConfigParser();
		self.config.read("conf/config.cfg")

		self.requestProcessor = RequestProcessor()


		self.host = self.config.get("server","host")
		self.port = self.config.getint("server","port")
		self.addr = (self.host, self.port)

		self.server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	def getHost(self):
		return self.host

	def getPort(self):
		return self.port

	def getHostByName(self, name):
		return socket.gethostbyname(name)

	def start(self):
		''' Start listening incoming requests '''
		
		self.server.bind( self.addr )
		self.server.listen(1000)

		print "Server started at: %s:%d"%(self.host, self.port)

		while True:
			conn, addr = self.server.accept()

			data = conn.recv(1000)

			if data:
				print "Data received:%s from %s"%(data,addr)

			response = self.requestProcessor.process(data)

			conn.send(response)


