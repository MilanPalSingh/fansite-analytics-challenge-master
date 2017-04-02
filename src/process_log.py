# your Python code to implement the features could be placed here
# note that you may use any language, there is no preference towards Python
import sys
import parser as pr
# global valiables 
file_name = "../insight_testsuite/tests/test_features/log_input/log.txt"
debug = False



# Main function - start point of the application
def main(argv):
	with open(file_name) as f:
		for line in f:
			pr.parser(line)


# main function call
if __name__ == "__main__":
    main(sys.argv)
