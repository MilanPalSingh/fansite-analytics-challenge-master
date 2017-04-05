"""
Feature 3
class defination for the Time window class
"""
import time
import utility as ut
# import requestClass as rc

class TimeW:
	timeList = []

	currentTime = 0

	range = 10

	def __init__(self, d, l ): 
		host, __ignore, __ignore, date, request, status, size = d
		self.date = ut.dt_parse(date)
		self.dateStr = date
		self.count = 0
		if TimeW.currentTime == 0:
			TimeW.currentTime = self.date
			self.count =1

	def orderList(self):
		# print "before sort"
		for i in range(len(TimeW.timeList)):
			if TimeW.timeList[i].timeDifL60():
				TimeW.timeList[i].count +=1
			# TimeW.timeList[i].display()

		TimeW.timeList.sort(key=lambda x: x.count, reverse=True)
		# print "after sort"

		if len(TimeW.timeList)>10:
			for i in reversed(range(10, len(TimeW.timeList))):
				if not TimeW.timeList[i].timeDifL60():
					TimeW.timeList.remove(TimeW.timeList[i])
		self.printToFile()

	def printToFile(self):
		thefile = open("../log_output/hours.txt", 'w')
		for i in range(len(TimeW.timeList)):
			if i<10:
				thefile.write(TimeW.timeList[i].display())
				thefile.write("\n")


	def timeDifL60(self):
		# self.display
		# print (self.date - TimeW.currentTime).total_seconds()
		if abs(( TimeW.currentTime - self.date ).total_seconds()) <= (60*60):
			return True
		else:
			return False

	def display(self):
		return self.dateStr+","+str(self.count)






