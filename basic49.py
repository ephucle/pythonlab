import sys
import os
from os.path import isfile, join

def listfiles(mypath):
	onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
	return onlyfiles

def main():
	#output = callcommand(sys.argv[1])
	
	mypath = sys.argv[1]
	print (mypath)
	files = listfiles(mypath)
	print (files)
	
	#pretty print
	print ( "\n".join(files) )
	

if __name__ == '__main__':
	main()