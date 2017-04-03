"""
class defination for the log
"""
import time
import utility as ut
import requestClass as rc


class Log:
	'Log class'
	# total log count 
	logCount = 0

	# max and min count of the most request host
	max = -1
	min = -1

	# range - for most active host
	range = 4

	# most frequent host
	freqHost = []


	def __init__(self, d ): 
		self.host, __ignore, __ignore, self.date, self.request, self.status, self.size = d
		self.date = ut.dt_parse(self.date)
		# ut.req_parser(self.request)
		ut.addToResList(self.request, self.size)
		# add to frequest host list if the the min is less than 1
		# self.request = rc.Request(ut.req_parser(self.request), self.size)
		self.count = 1
		self.rank = 0 # range 1-10
		# inc the global request count
		Log.logCount += 1
		self.addToFreqHostList()


	def addCount(self, req, size):
		Log.logCount += 1
		# self.request.count +=1
		self.count += 1 
		ut.addToResList(req, size)
		self.addToFreqHostList()


	def getCount(self):
		return self.count

	def addToFreqHostList(self):
		# if ut.debug: print "size of the list", len(Log.range)
		if Log.min < self.count :
			if self in Log.freqHost:
				self.resetRanks()
			# else:
			else:
				if len(Log.freqHost) < Log.range :
					Log.freqHost.append(self)
				else:
					# del the last element and reset it's rank to 0
					Log.freqHost[Log.range-1].changeRank(0)
					Log.freqHost.remove(Log.freqHost[Log.range-1])
					# add the obj to the last
					Log.freqHost.append(self)
				self.resetRanks()


	def changeRank(self, r):
		self.rank = r
		# self.resetRanks()



	def display(self):
		print self.host , self.count , self.rank#, self.request.display()

	def isEqual(self, obj):
		return True if self.count > obj.count else False

	# def printFreqHost(self):
	# 	for l in freqHost:
	# 		l.display()

	def resetRanks(self):
		Log.freqHost.sort(key=lambda x: x.count, reverse=True)
		# Log.freqHost = ut.sortReq(Log.freqHost)
		for l in Log.freqHost:
			if l.rank != (Log.freqHost.index(l)+1):
				l.changeRank(Log.freqHost.index(l)+1)
				if len(Log.freqHost) < Log.range :
					Log.min = -1
				else:
					Log.min = Log.freqHost[Log.range - 1].count
				Log.max = Log.freqHost[0].count
		ut.writeFreqToFile(Log.freqHost) 










		
