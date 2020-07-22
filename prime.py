#!/usr/bin/env python3
from timeit import default_timer as timer

#dong nao giai bai toan tim so nguyen so
input_number = input ("Enter a number: ")
n = int(input_number)


primes = [1,2]
#print(primes)
#i bat dau la so 2, rang tu 2 toi 99


start = timer()


for i in range(2,n):
	prime=True
	#j bat dau la so 3
	for j in range(2,i):
		if i%j == 0:
			
			#print(i, "=",j, "*", i//j)
			prime=False
			break
	if prime == True:
		#print(i, " is prime")
		if i not in primes:
			primes.append(i)
		prime=False

end = timer()

print("Duration ", end - start)
print("List of primes number from 0 to ", n , " is :")
print(primes)

#giai quyet vu thieu so 19
