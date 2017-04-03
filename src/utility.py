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

""" global valiables """

# input file name and path  
file_name = "../insight_testsuite/tests/test_features/log_input/log.txt"

# debug flage
# debug = True
debug = False


# Global List of Log objects
logList = {}


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
def addToLogList(obj):
	# if debug :	obj.display()
	host, __ignore, __ignore, date, request, status, size = obj

	# if the host exsists in the list
	if logList.has_key(host):
		logList[host].addCount()
	else:
		logList[host] = lc.Log(obj)
		# add to frequest host list if the the min is less than 1



def printList():
	for o in logList.keys():
		logList[o].display()
	print lc.Log.logCount


def writeToFile(fileName, list):
	thefile = open(fileName, 'w')
	for item in list:
		thefile.write("%s, %s\n" % item.host, item.count)

def writeFreqToFile(list):
	thefile = open("../log_output/hosts.txt", 'w')
	for item in list:
		thefile.write(item.host + ", " + str(item.count)+ "\n")

def sortReq(list):
	return  sorted(list, key=lambda x: x.count, reverse=True)







