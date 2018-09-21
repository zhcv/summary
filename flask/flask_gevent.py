# coding=utf-8

from flask import Flask, request, g
import flask
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()
# gevent end

import time

app = Flask(__name__)
app.config.update(DEBUG=True)

@app.route('/user/<name>')
def user(name=None):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/asyn/', methods=['GET'])
def test_asyn_one():
    arg = request.args
    print arg
    print("asyn has a request!")
    # time.sleep(10)
    return flask.jsonify({"has_result": "True",
                          "result": "hello asyn"
                         }
                        )


@app.route('/test/', methods=['GET'])
def test():
    return flask.jsonify({"has_result": "True",
                          "result": "hello test"
                         }
                        )


if __name__ == "__main__":
    # app.run()
    http_server = WSGIServer(('', 5123), app)
    http_server.serve_forever()
