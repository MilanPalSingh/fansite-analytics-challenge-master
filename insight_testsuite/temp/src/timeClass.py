"""
Feature 3
class defination for the Time-window class


"""
import time
import utility as ut

class TimeW:

	# List if the Time-window objects
	timeList = []

	# class global variable for current time
	currentTime = 0

	# Number of top variables to be printed
	range = 10

	# window size in minites
	minWindow = 60

	# intlazation of the Time window Class
	def __init__(self, d, l ): 
		host, __ignore, __ignore, date, request, status, size = d
		self.date = ut.dt_parse(date)
		self.dateStr = date
		self.count = 0
		if TimeW.currentTime == 0:
			TimeW.currentTime = self.date
			self.count =1

	# order the time list 
	def orderList(self):
		# increase the count of all time obj with time diffrance less than minWindow
		for i in range(len(TimeW.timeList)):
			if TimeW.timeList[i].timeDifL60():
				TimeW.timeList[i].count +=1
			# TimeW.timeList[i].display()

		# sort the list
		TimeW.timeList.sort(key=lambda x: x.count, reverse=True)
		# print "after sort"

		# remove the time obj from list that will never make it to top range
		if len(TimeW.timeList)>TimeW.range:
			for i in reversed(range(TimeW.range, len(TimeW.timeList))):
				if not TimeW.timeList[i].timeDifL60():
					TimeW.timeList.remove(TimeW.timeList[i])
		self.printToFile()

	# print to the file hours
	def printToFile(self):
		thefile = open(ut.fileHours, 'w')
		for i in range(len(TimeW.timeList)):
			if i<TimeW.range:
				thefile.write(TimeW.timeList[i].display())
				thefile.write("\n")


	# check the time diffrance with the current time 
	def timeDifL60(self):
		# self.display
		# print (self.date - TimeW.currentTime).total_seconds()
		if abs(( TimeW.currentTime - self.date ).total_seconds()) <= (60*TimeW.minWindow):
			return True
		else:
			return False

	# format the string to print to file
	def display(self):
		return self.dateStr+","+str(self.count)






