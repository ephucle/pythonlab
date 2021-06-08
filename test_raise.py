x = "hello"
x= 5
if not type(x) is int:
  raise TypeError("Only integers are allowed")

print("something after raise")