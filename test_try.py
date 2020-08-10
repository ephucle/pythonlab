def main(): 
   try: 
      func() 
      print("print this after function call") 
   except ZeroDivisionError: 
      print('Divided By Zero! Not Possible! ') 
   except: 
      print('Its an Exception!') 
def func(): 
   print(1/0) 
main()
