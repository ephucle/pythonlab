import sys
import subprocess
#cmd = sys.argv[1]
#print (cmd)


def callcommand(cmd):
	(status ,output ) = subprocess.getstatusoutput(cmd)
	if status ==0 :
		#print (output)
		return output

def main():
	output = callcommand(sys.argv[1])
	print (output)
	

if __name__ == '__main__':
	main()