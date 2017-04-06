"""
class defination for the Request
"""
import time
import utility as ut


class Request:
	# globle total number of counts
	reqCount = 0
	# reqSize = 0

	# number of frequent resources 
	range = 10
	min = -1
	max  = -1
	# list of top frequent resources  
	freqRes=[]

	# initilization function
	def __init__(self, d , size):
		self.res = d
		self.count = 1 
		if size == "-\n":
			self.size =0
		else:
			self.size = int(size)
		self.rank = -1
		Request.reqCount += 1
		self.addToFreqResList()

	# orint function for debuge
	def display(self):
		print self.res, self.size

	# add the size of the request to the resourse object
	def addSize(self, size):
		Request.reqCount += 1
		# self.request.count +=1
		if size == "-\n":
			self.size += 0
		else:
			self.size += int(size )
		self.addToFreqResList()

	# manage the Resource List - sort them according to size of the resource request
	def addToFreqResList(self):
		# if ut.debug: print "size of the list", len(Log.range)
		if Request.min < self.size :
			# check the current obj is in the Frequest list
			# if yes:
			if self in Request.freqRes:
				self.resetRanks()
			# else:
			else:
				if len(Request.freqRes) < Request.range :
					Request.freqRes.append(self)
				else:
					# del the last element and reset it's rank to 0
					Request.freqRes[Request.range-1].changeRank(0)
					Request.freqRes.remove(Request.freqRes[Request.range-1])
					# add the obj to the last
					Request.freqRes.append(self)
				self.resetRanks()

	# change rank of the resource
	def changeRank(self, r):
		self.rank = r
		# self.resetRanks()


	# rank of the resource reset after the sort- and write to the file
	def resetRanks(self):
		Request.freqRes.sort(key=lambda x: x.size, reverse=True)
		# Request.freqRes = ut.sortReq(Request.freqRes)
		for l in Request.freqRes:
			if l.rank != (Request.freqRes.index(l)+1):
				l.changeRank(Request.freqRes.index(l)+1)
				if len(Request.freqRes) < Request.range :
					Request.min = -1
				else:
					Request.min = Request.freqRes[Request.range - 1].count
				Request.max = Request.freqRes[0].count
		ut.writeResToFile(Request.freqRes) 



