from flask import *
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('Frontend-2.html')
@app.route('/l', methods=['POST'])
def login():
    uname = request.form['uname']
    passwrd = request.form['pass']
    if uname == "deepak" and passwrd == "123":
        return "<h1><center><font color = 'blue'><br><br><br><b><i>Welcome %s </i></b></font></center><h1>" % uname
    else:
        return "<h1><center><font color = 'red'><br><br><br><b>Wrong Username and password</b></font></h1></center>"
if __name__ == '__main__':
    app.run(debug=True)