import os
from flask import Flask
import pync

app = Flask(__name__)


@app.route('/')
def hello_world():
    pync.notify('For details.', open='http://github.com/', title='Github')
    return 'Hello, girls! ' + os.F_TLOCK.__str__()


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='localhost')
