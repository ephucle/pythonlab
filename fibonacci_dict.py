from myfunc import Timer
t=Timer()

known = {0:0, 1:1}
print(known)
#dung dict de luu data, do mat cong tinh lai
def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

#ham de quy
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

t.start()
print(f'fibonacci(50) ={fibonacci(50)}')
t.stop()

t.start()
print(f'fibonacci(70) ={fibonacci(70)}')
t.stop()

print("*"*30)
t.start()
print(f'recur_fibo(15) ={recur_fibo(15)}')
t.stop()

t.start()
print(f'recur_fibo(40) ={recur_fibo(40)}')
t.stop()


