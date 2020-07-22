from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def home():
	return 'Home page'
	
@app.route('/user')
def user():
	return 'User page'

@app.route('/about')
def about():
	return 'About page'

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return 'User %s' % escape(username)
	#return 'Hello %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return 'Subpath %s' % subpath

if __name__ == '__main__':
	app.run()