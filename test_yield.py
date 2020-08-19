def f(value):
	print("run to before while")
	while True:
		print("inside while, before yield")
		value = (yield value)
		print(f"check value = (yield value): {value}")
		#yield value
		print("inside while, after yield")

a=f(10)
print(type(a))  #<class 'generator'>

print("---call first next(a)")
print(next(a))

print("---call second next(a)")
print(next(a))


print("---call 3rd next(a)")
print(next(a))

print(">>>> call a.send(20)")
print(a.send(20))  # reset gia tri value ve 20

print(">>>> call a.send(30)")
print(a.send(30))