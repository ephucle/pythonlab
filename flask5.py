from flask import Flask
from flask import render_template
#Để lấy dữ liệu form. bạn cần import module request của flask. Sử dụng request.from['key'] để lấy giá trị của trường ‘key’
from flask import request

app = Flask(__name__)
 
#@app.route('/')
#def hello_world():
#    return 'Hello, World!'

@app.route('/')
def home():
    return 'Home page'
 
 
@app.route('/user')
def user():
    return 'User page'
 
 
@app.route('/about')
def about():
    return 'About page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()