# -*-coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return '<h1><a href ="/flask">hello, flask</a></h1>'

def hello():
    return '<h1><a href="/">root</a></h1>'


if __name__ == '__main__':
    app.run()