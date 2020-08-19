from myfunc import cat
def parse_csv2(file, seperator="!", commentor="#"):
	'''
	>>> parse_csv('b.csv')
	[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5'], ['4', '5', '6']]
	'''
	#lines_new = [line.strip().split('!') for line in lines if not line.startswith('#')]
	lines = open(file).readlines()
	lines_new = [line.strip().split(seperator) for line in lines if not line.startswith(commentor)]
	return lines_new
filename = 'b.csv'
cat(filename)

def convert_separator_csv(outfile='c.csv', infile='b.csv' , oldseperator="!", newseperator=";"):
	data = parse_csv2(infile, seperator="!", commentor="#")
	with open(outfile, 'w') as outfile:
		for row in data:
			new_row = newseperator.join(row)
			outfile.write(new_row +"\n")

convert_separator_csv(outfile= 'c.csv', infile='b.csv' , oldseperator="!", newseperator=";")

cat('c.csv')