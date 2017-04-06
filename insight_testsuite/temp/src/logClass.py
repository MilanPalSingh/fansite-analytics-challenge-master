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


	# initilization
	def __init__(self, d, l ): 
		self.host, __ignore, __ignore, self.date, self.request, self.status, self.size = d
		self.date = ut.dt_parse(self.date)
		ut.addToResList(self.request, self.size)
		self.count = 1
		self.rank = 0 # range 1-10
		# inc the global request count
		Log.logCount += 1
		
		# add to List of hosts and there frequency of request 
		self.addToFreqHostList()

		# list for past consicutive login fails for the host
		self.logInFailTime = []

		# set the flage if the host it blocked
		self.isBlocked = False 

		# start of the block time
		self.blockTime = self.date 
		
		# function to check the present request
		self.checkReq(self.request, self.status, self.date, l)



	# if the host obj pre exists increase the count
	def addCount(self, req, size, status, date, l ):
		Log.logCount += 1
		# self.request.count +=1
		self.count += 1 
		ut.addToResList(req, size)
		self.addToFreqHostList()
		self.checkReq( req, status, date, l)


	# return the current count of the host
	def getCount(self):
		return self.count

	# sort the host list on the count value and write to the file
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


	# set the rank of the current obj
	def changeRank(self, r):
		self.rank = r
		# self.resetRanks()


	# print function for deguging
	def display(self):
		print self.host , self.count , self.rank#, self.request.display()


	# set rank based on the sorting
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

	
	# function takes 3 parameters { request, status, log to be written to the file }
	# check if the host is blocked or not
	def checkReq(self, req, status, date,  log):
		# if ut.debug: print log , self.isBlocked
		if self.isBlocked :
			if self.isDifLess5(date):
				# if ut.debug: print "write to the file"
				ut.appendToFile(ut.fileBlocked, log)
				return 
			else:
				self.isBlocked = False
				self.logInFailTime = []

		if self.isLoginFail(req, status):
			self.logInFailTime.append(date)
			self.resetBlock()

		
		# add to check the time
		# if(!self.isBlocked):
		# 	if(self.isLoginFail(req,status)):
		# 		pass
		# else:
		# 	ut.appendToFile("../log_output/blocked.txt ", log)


	def isLoginFail(self, req, status):
		typ , r, proto  = ut.req_parser(req)
		if (int(status)==401) and (r == "/login"):
			return True
		else:
			return False

	def isDifLess5(self, d):
		# if ut.debug: print "minutes: ",(d - self.blockTime ).total_seconds()/(5*60)
		if (d - self.blockTime ).total_seconds() > (5*60):
			return False
		else:
			return True

	def isDifLess20(self, d1, d2):
		# if ut.debug: print "seconds: ",(d2 - d1 ).total_seconds()
		if (d2 - d1).total_seconds() >20:
			return False
		else:
			return True


	def resetBlock(self):

		# check with thrid element if the time is less than 5 min del the last element if not del the 
		# if self.isBlocked:

		# check with the last entry with the time from the start and del which ever is greater than 20 sec
		# elif len(self.logInFailTime) >1:
		l = len(self.logInFailTime)
		for i in range(0, l -1):
			if self.isDifLess20(self.logInFailTime[i] , self.logInFailTime[l-1] ):
				break
			else:
				self.logInFailTime.remove(self.logInFailTime[i])


		if len(self.logInFailTime) ==3:
			self.isBlocked = True
			self.blockTime = self.logInFailTime[2]
		else: 
			self.isBlocked = False

		# return self.isBlocked






		
