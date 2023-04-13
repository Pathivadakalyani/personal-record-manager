
'''from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/fail')
def index():
    return 'you are failed'
@app.route('/input/<float:number>')
def user(number):
    if number>=35.0:
        return redirect(url_for('third'))
    else:
        return redirect(url_for('index'))
@app.route('/pass')
def third():
    return 'you are passed'
app.run(debug=True,use_reloader=True)'''

#redirecting to the dynamic row

from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/userinput/<float:number>')
def uinput(num):
    if number>100:
        return 'invalid marks'
    else:
        return redirect(url_for('user',number=num)
@app.route('/fail')
def index():
    return 'you are failed'
@app.route('/input/<flosat:number>')
def user(number):
    if number>=35.0:
        return('http://127.0.0.1:5000/pass')
    else:
        return('http://127.0.0.1:5000/fail')

@app.route('/pass)
def third():
    return 'you are passed'
app.run(debug=True,use_reloader=True)

