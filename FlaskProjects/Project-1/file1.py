from flask import Flask, render_template

klu = Flask(__name__)


@klu.route('/')
def hello():
    return 'Hello, World!'
@klu.route('/fun')
def function1():
    return 'nivesh welcome'
@klu.route('/fun2')
def function2():
    return render_template('Frontend1.html')
if __name__ == '__main__':
    klu.run()