# coding: utf-8
'''app '''
from __future__ import unicode_literals
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    """
    hello console
    """
    
    return "hello"


if __name__ == '__main__':
    app.run()