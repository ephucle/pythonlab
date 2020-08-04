#https://runestone.academy/runestone/books/published/thinkcspy/WebApps/07-InputForAFlaskWebApplication.html
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
	#name = request.args['name']
	#if 'name' in request.args:
	#	name = request.args['name']
	#else:
	#	name = 'World'
	
	#cach ngan gon hon
	name = request.args.get('name', 'World')

	
	#http://localhost:5000/?name=Frank
	return """
			<html><body>
			<h1>Hello, {0}!</h1>
			The time is {1}.
			</body></html>
			""".format(
			name, str(datetime.now()))

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)