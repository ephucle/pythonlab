def parse_csv2(file, seperator="!", commentor="#"):
	'''
	>>> parse_csv('b.csv')
	[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5'], ['4', '5', '6']]
	'''
	
	
	#lines_new = [line.strip().split('!') for line in lines if not line.startswith('#')]
	lines = open(file).readlines()
	lines_new = [line.strip().split(seperator) for line in lines if not line.startswith(commentor)]
	return lines_new