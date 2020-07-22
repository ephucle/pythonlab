#https://stackoverflow.com/questions/23484491/flask-streaming-data-by-writing-to-client

from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/loop')
def loop():
    def generate():
        yield "Hello"
        yield "World"
    return Response(generate())

@app.route('/longloop/<int:rows>')
def longloop(rows):
    def generate(rows):
        for i in range(rows):
            yield "{i}: Hello World".format(i=i)
    return Response(generate(rows))

if __name__ == '__main__':
    app.run(debug=True)