import sys
args = sys.argv[1:]
#print (args)
if len(args) !=3: 
	print("wrong input")
	sys.exit()

amt1 = float(args[0])
int1 = float(args[1])
year1 = int(args[2])

#print (amt1,int1,year1)
def saving(amt,interest,year):
	for i in range(year):
		lai =  interest*amt/100
		amt = amt + lai
	return amt

def main():
	save = saving(amt1,int1,year1)
	print("So tien se nhan duoc khi goi", amt1, " voi lai suat", int1, "sau", year1, "se nhan duoc:",save)

if __name__ == '__main__':
	main()