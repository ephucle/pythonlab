import sys
import os

#print ("script name", sys.argv[0])

def callcommand(cmd):
	(status ,output ) = subprocess.getstatusoutput(cmd)
	if status ==0 :
		#print (output)
		return output

def main():
	#output = callcommand(sys.argv[1])
	#print (output)
	print ("Script name:", sys.argv[0])
	print(os.path.realpath(__file__))
	
	#cach 2 lay current script name
	print (__file__)

if __name__ == '__main__':
	main()