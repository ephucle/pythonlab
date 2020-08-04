#!/usr/bin/env python
#https://runestone.academy/runestone/books/published/thinkcspy/WebApps/08-WebApplicationsWithAUserInterface.html

from flask import Flask, request
from datetime import datetime
import re

with open('emma.txt') as infile:
	#full text to test regex
	text = infile.read()

with open('emma.txt') as infile:
	
	lines = [line.strip() for line in infile.readlines()]


#print(lines)

app = Flask(__name__)

@app.route('/')
def home():
	
	return """
         <html><body>
             <h2>Welcome to the Greeter</h2>
             <form action="/greet">
                 Regex pattern <input type='text' name='regex_pat'><br>
                 Some more variable can be created here? <input type='text' name='favfood'><br>
                 <input type='submit' value='Regex matching'>
             </form>
             <h2> SAMPLE TEXT to text REGEX{0} </h2>
         </body></html>
         """.format(text)

@app.route('/greet')
def greet():
	regex_pat = request.args.get('regex_pat', 'World')
	favfood = request.args['favfood']
	if favfood == '':
		msg = 'You did not tell me your favorite food.'
	else:
		msg = 'I like ' + favfood + ', too.'
	
	
	
	
	m = re.findall(regex_pat,text)
	matching_patterns = []
	if m:
		print ("match pattern found")
		matching_patterns = str(m)  #convert list to string
		#print(matching_patterns)
	else:
		print ("not match")
		matching_patterns = "n/a"
		

	matching_lines = []
	for line in lines:
		if re.search(regex_pat, line):
			matching_lines.append(line)
	
	print("Matching lines:")
	print(matching_lines)

	return """
         <html><body>
             <h2>Your input pattern is: {0}</h2>
             {1}
             <h2>Matching pattern as below </h2>:
             {2}
             <h2> All Matching lines as below </h2>

         </body></html>
         """.format(regex_pat, matching_patterns,"\n".join(matching_lines))

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)