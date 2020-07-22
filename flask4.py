#https://mortoray.com/2014/03/04/http-streaming-of-command-output-in-python-flask/
import flask
from shelljob import proc

app = flask.Flask(__name__)

@app.route( '/stream' )
def stream():
    g = proc.Group()
    p = g.run( [ "bash", "-c", "for ((i=0;i<100;i=i+1)); do echo $i; sleep 1; done" ] )

    def read_process():
        while g.is_pending():
            lines = g.readlines()
            for proc, line in lines:
                yield line

    return flask.Response( read_process(), mimetype= 'text/plain' )

if __name__ == "__main__":
    app.run(debug=True)