# -*-coding:utf-8 -*-

from flask import Flask


app = Flask(__name__)

@app.route('/')
def root():
    return '<h1><a href ="/test/admin">test</a></h1>'


@app.route('/test/<id>')
def test(id):
    return f'<h1>hello, {id}</h1>'


if __name__ == '__main__':
    app.run(port='5600')