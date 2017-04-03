"""
class defination for the Request
"""
import time
import utility as ut


class Request:
	reqCount = 0
	reqSize = 0

	def __init__(self, d ):
		self.type , self.res, self.proto  = d
		self.count = 1 
		Request.reqCount += 1

	def display(self):
		print self.type , self.res

