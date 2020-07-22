def cumulative_sum(l):
	new_l = []
	new_l.append(l[0])
	for i in range(1,len(l)):
		new_l.append(l[i] + new_l[-1])
	return new_l

print(f'cumulative_sum([1,2,3]) = {cumulative_sum([1,2,3])}' )
print(f'cumulative_sum([1,2,3,4,5,6,7,8,9,10]) = {cumulative_sum([1,2,3,4,5,6,7,8,9,10])}' )