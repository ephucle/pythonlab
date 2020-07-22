import sys
#stack_diagram.py

def b(z):
    prod = a(z, z)
    print (z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    print("start func...")
    print(f"c input: x = {x}, y= {y} z={z}")
    total = x + y + z
    print(f"total = {total}")
    square = b(total)**2
    print(f'b(total) = {b(total)}')
    print(f'square = b(total)**2 = {square}')
    return square

x = 1
y = x + 1
print('x=',x, 'y=',y)
#sys.exit()

print("call c func")
print (c(x, y+3, x+y))
