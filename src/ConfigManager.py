#!/usr/bin/env python

CONFIG_FILE="/home/max/Dropbox/study/6th_course/diploma/MNC/conf/config.cfg"

import ConfigParser

class ConfigManager:
	_config = ConfigParser.RawConfigParser()
	_config.read(CONFIG_FILE)

	def getServerHost(self): #return socket server host name
		return self._config.get("server","host")

	def getServerPort(self): #return socket server listen port
		return self._config.getint("server","port")


	def getDbLocation(self):
		return self._config.get("database","location")

	def getDb(self):
		return self._config.get("database","db")

	def getTestDb(self):
		return self._config.get("database","test_db")

