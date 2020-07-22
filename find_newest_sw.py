sw_filter_list = set(['CXP9024418/12_R54B47' ,'CXP9024418/12_R57C74', 'CXP9024418/12_R60B28' , 'CXP9024418/6_R77B39' , 'CXP9024418/6_R80F30' ,  'CXP9024418/6_R85C103(gNB)'])

s1 = {'CXP9024418/6_R73C96', 'CXP9024418/6_R71B34', 'CXP9024418/6_R73E32'}
s2 = {'CXP9024418/6_R80C90(gNB)', 'CXP9024418/12_R54B47', 'CXP9024418/6_R73E32', 'CXP9024418/6_R73C96'}

s3 = {'CXP9024418/12_R54B47', 'CXP9024418/12_R60B28'}
s4 ={'CXP9024418/6_R73C96', 'CXP9024418/6_R71B34'}
s5 = { 'CXP9024418/12_R54B47', 'CXP9024418/12_R55B26'}
s6 ={'CXP9024418/6_R80C90(gNB)'}
s7 = {'CXP9024418/6_R80C90(gNB)', 'CXP9024418/6_R73E32', 'CXP9024418/6_R73C96'}

print (sw_filter_list)

def find_newest_pkg(sw_set):
	result = []
	sw6 = []
	for item in sw_set:
		if "/6" in item and "gNB" not in item:
			sw6.append(item)
	sw6 = sorted(sw6)
	
	sw12 = []
	for item in sw_set:
		if "/12" in item:
			sw12.append(item)
	sw12 = sorted(sw12)
	
	sw5 = []
	for item in sw_set:
		if "/5" in item:
			sw5.append(item)
	sw5 = sorted(sw5)
	
	sw4t = []
	for item in sw_set:
		if "gNB" in item:
			sw4t.append(item)
	sw4t = sorted(sw4t)
	
	if len(sw5) > 0: result.append(sw5[-1])
	if len(sw6) > 0: result.append(sw6[-1])
	if len(sw12) > 0: result.append(sw12[-1])
	if len(sw4t) > 0: result.append(sw4t[-1])
	
	return set(result)

print("test s1")
print(s1)
print(find_newest_pkg(s1))


print("test s2")
print(s2)
print(find_newest_pkg(s2))

print("test s3")
print(s3)
print(find_newest_pkg(s3))

print("test s4")
print(s4)
print(find_newest_pkg(s4))

print("test s5")
print(s5)
print(find_newest_pkg(s5))

print("test s6")
print(s6)
print(find_newest_pkg(s6))

print("test s7")
print(s7)
print(find_newest_pkg(s7))