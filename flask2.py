from __future__ import print_function # In python 2.7
#!/usr/bin/env python3
#https://www.reddit.com/r/learnpython/comments/3qsiva/tutorials_on_how_to_run_my_script_in_browser_with/

from flask import Flask, stream_with_context, request, Response, url_for
from flask import render_template

from datetime import datetime as dt


import sys

now = dt.now()

app = Flask(__name__)

@app.route('/simple-stream')
def streamed_response():
	return Response(stream_with_context(generate()))

def generate():
	yield str(now)
	


@app.route('/test')
def test():
	return 'Hello World' + str(1) 


@app.route('/button/')
def button_clicked():
    print('Hello world!', file=sys.stderr)
    return redirect('/')
	
	
if __name__ == "__main__":
	app.run(use_reloader=True,debug=True)