"""# Parser - read the line from the log and extract the component 

import logClass


p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')

def parser(l):
	m = p.match(l)
	o = logClass.Log(m.groups())
	o.print()





# main function call
if __name__ == "__main__":
    parser()
