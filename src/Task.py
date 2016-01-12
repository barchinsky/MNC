#!/usr/bin/env python

'''
	This class implemets base structure of tasks for monitoring devices.
'''

class Taks:
	def __init__(self):
		self._id = None
		self._type = None # Ground | Flying
		self._status = None # New | In progress | Done
		self._manageType = None # Manual | Autonomous | Mixed
		self._description = None