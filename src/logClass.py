# class defination for the log

import time
from datetime import datetime,timedelta

def dt_parse(t):
    ret = datetime.strptime(t[0:20],'%d/%b/%Y:%H:%M:%S')
    if t[22]=='+':
        ret-=timedelta(hours=int(t[23:26]),minutes=int(t[27:]))
    elif t[22]=='-':
        ret+=timedelta(hours=int(t[23:26]),minutes=int(t[27:]))
    return ret


class Log:
	'Log class'
	logCount = 0

	def __init__(self, d ): #[host, ignore, user, date, request, status, size]):
		self.host, __ignore, __ignore, self.date, self.request, self.status, self.size = d
		# self.host = host
		# self.date = time.strftime(self.date)
		# self.date = datetime.strptime(self.date, '%d/%b/%Y:%H:%M:%S %z')
		# self.request = request
		# self.status = status
		# self.size = size
		# self.requestCount = 1
		Log.logCount += 1
		# print "inside the class"

	def addCount(self):
		self.requestCount +=1

	def display(self):
		print self.date
		d = dt_parse(self.date)
		print d.minute