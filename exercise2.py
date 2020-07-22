import itertools

result = []
for c in itertools.permutations('aeiou', 5):
	#print(c)
	#('u', 'a', 'o', 'i', 'e')
	text = ''.join(c)
	result.append(text)

print("Count:", len(result))
print(result)
