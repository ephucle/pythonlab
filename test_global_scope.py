def f(value, values, dict1):
	v = 1
	values[0] = 44
	dict1['key1'] = 'value1'
t = 3
v = [1, 2, 3]
d = {'a':1, 'b':2}
print("before", t, v, d)
f(t, v, d)
print("after", t, v, d)

a = 10

