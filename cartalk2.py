import time
start = time.perf_counter()
digits = '0123456789'
def is_palindromic(string_of_numbers):
	reversed_string_of_numbers = "".join(string_of_numbers[::-1])
	if string_of_numbers == reversed_string_of_numbers: return True
	else: return False

#print(is_palindromic('12321'))
#print(is_palindromic('123321'))
#print(is_palindromic('1236321'))
#print(is_palindromic('1122'))
#print(is_palindromic('11223'))
#print(is_palindromic('9'))


list_of_six_numbers = [n1+n2+n3+n4+n5+n6 for n1 in digits for n2 in digits for n3 in digits for n4 in digits for n5 in digits for n6 in digits]

palindromic_number = [number for number in list_of_six_numbers if is_palindromic(number)]

print(palindromic_number)
print("No of 6 digits and palindromic number  found", len(palindromic_number))


end = time.perf_counter()
duration = end - start
print("Duration:", duration)