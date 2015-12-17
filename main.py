#!/usr/bin/env python

try:
	from src import Server
except NameError as e:
	print "Import module error:%s" %(e)

def test():
	print "Test";


if __name__ == "__main__":
	server = Server()
	#print server.getHost(), server.getPort()
	server.start()