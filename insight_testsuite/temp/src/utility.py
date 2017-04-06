""" 
utility functions 
	dt_parse(t):	t- string with the time format [10/Oct/2000:13:55:36 -0700]
		return: 	datetime object 
	parser(l):		l- string with comman log format {127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326}
		return:		groups - [host, ignore, user, date, request, status, size]
"""
import re
from datetime import datetime,timedelta
import logClass as lc
import requestClass as rc
import timeClass as tc

""" global valiables """

# path = "../"
path = ""

# input file name and path  
file_name = path+ "log_input/log.txt"
fileHours = path+"log_output/hours.txt"
fileBlocked = path+"log_output/blocked.txt"
fileHosts = path+"log_output/hosts.txt"
fileRes = path+"log_output/resources.txt"
# debug flage
# debug = True
debug = False


# Global dict of Log objects
logList = {}

# Global dict of resource objects
resList = {}


""" END: global valiables """


# function to parse the time format [10/Oct/2000:13:55:36 -0700] is the date, time, and time zone
def dt_parse(t):
	# regular expression for parsing the date
    ret = datetime.strptime(t[0:20],'%d/%b/%Y:%H:%M:%S')

    # to add the time zone
    if t[22]=='+':
        ret-=timedelta(hours=int(t[23:26]),minutes=int(t[27:]))
    elif t[22]=='-':
        ret+=timedelta(hours=int(t[23:26]),minutes=int(t[27:]))
    return ret


# Fucntion to parse the log string 
def parser(l):
	# regular expression for parsing the log format
	p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')
	m = p.match(l)
	return m.groups()

# Function to parse the request parameters 
def req_parser(r):
	# print r.split()
	return r.split()

# add the log object to the globle log list "logList"
def addToLogList(obj, l):
	# if debug :	obj.display()
	host, __ignore, __ignore, date, request, status, size = obj

	# if the host exsists in the list
	if logList.has_key(host):
		logList[host].addCount(request,size, status, dt_parse(date), l)
	else:
		logList[host] = lc.Log(obj, l)
		# add to frequest host list if the the min is less than 1





# for feature 3 
def addToTimeList(obj, l):
	host, __ignore, __ignore, date, request, status, size = obj

	if len(tc.TimeW.timeList) == 0:
		tc.TimeW.timeList.append(tc.TimeW(obj,l))
	elif tc.TimeW.currentTime != dt_parse(date):
		tc.TimeW.timeList.append(tc.TimeW(obj,l))
		tc.TimeW.currentTime = dt_parse(date)
		tc.TimeW.timeList[len(tc.TimeW.timeList)-1].orderList()
	else:
		tc.TimeW.timeList[len(tc.TimeW.timeList)-1].orderList()


	

def addToResList(res, size):
	typ , r, proto  = req_parser(res)

	if resList.has_key(r):
		resList[r].addSize(size)
	else:
		resList[r] = rc.Request(r, size )

# used for debuging 
def printList():
	for o in logList.keys():
		logList[o].display()
	print lc.Log.logCount

# used for debuging
def printResList():
	for o in resList.keys():
		# print o
		resList[o].display()
	print rc.Request.reqCount  


# append l to the given file name
def appendToFile(fileName, l):
	thefile = open(fileName, 'a')
	thefile.write( l )

# write to the hosts file
def writeFreqToFile(list):
	thefile = open(fileHosts, 'w')
	for item in list:
		thefile.write(item.host + "," + str(item.count)+ "\n")

# sort the obj list on obj varable count
def sortReq(list):
	return  sorted(list, key=lambda x: x.count, reverse=True)

# write to the resources file 
def writeResToFile(list):
	thefile = open(fileRes, 'w')
	for item in list:
		thefile.write(item.res + "\n")#+ ", " + str(item.size)+ "\n")







