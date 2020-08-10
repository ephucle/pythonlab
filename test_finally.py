
def f():
	try:
		print("Doan code nam ben tren except")
		#print(1/0)
		#print(2+'a')
		
		print("Doan code nam ben duoi except")
	except ZeroDivisionError:
		print("Chia cho zero")
	except TypeError:
		print("da chay vao type error")
	except:
		print("Total except")
	else:
		print("neu trong try khong co loi thi se chay doan ELSE nay")
	finally:
		print("Doan cod ben trong finally")
	
j=f()