# your Python code to implement the features could be placed here
# note that you may use any language, there is no preference towards Python
import sys
import utility as ut
import logClass as lc
import requestClass as rc





def processLog(line):
	# parse the log file and creat the Log object 
	# obj = lc.Log(ut.parser(line))
	# debug statment 
	# if ut.debug :	obj.display()
	ut.addToLogList(ut.parser(line), line)
	ut.addToTimeList(ut.parser(line), line)





# Main function - start point of the application
def main(argv):
	# open file and read line by line
	with open(ut.file_name) as f:
		for line in f:
			processLog(line)

	if ut.debug:	
		ut.printList()
		print "print the freq List"
		for l in lc.Log.freqHost:
			l.display()
		print "print the res list"
		ut.printResList()
		print "print the freq List"
		for l in rc.Request.freqRes:
			l.display()


# main function call
if __name__ == "__main__":
    main(sys.argv)
