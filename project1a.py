import sys
import math

def calpi(n):
	pi = round(math.pi,n)
	return pi

def calpi2(n):
	pitemp ="3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127360"
	list1 = pitemp.split(".")
	#print(pitemp)
	#print (list1)
	pi_string = list1[0] + '.' + list1[1][:n]
	return pi_string

def calpi3(n):
	#π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - 4/(12*13*14) ...
	pi3 = 3
	
	for i  in range(1, 1000000):
		n1 = 2*i
		n2 = 2*i +1
		n3 = 2*i+2 
		#print (n1, n2, n3)
		pi3 += (-1)**(i+1) * 4/(n1*n2*n3)
	#print (pi3)
	pi3 = round(pi3,n)
	return pi3

def main():
	#nho chuyen doi n sang so nguyen, loi hoai
	n = int(sys.argv[1])
	
	#print tim pi cach 1
	print ("lay gia tri pi tu module math")
	pi = calpi(n)
	print (pi)
	
	#print pi theo cach 2
	print ("pi value from bigfloat module")
	pi2 = calpi2(n)
	print (pi2)
	
	#print tim pi cach 3
	print ("Tinh bang cong thuc 4")
	pi3 = calpi3(n)
	print(pi3)

if __name__ == '__main__':
	main()