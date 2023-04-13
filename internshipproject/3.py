'''from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
app.run()'''

#when user pass request we use arguements in the link to get output
'''from flask import Flask,request
app=Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
@app.route('/second')
def second():
    print(request.method)
    print(request.args.get('user'))
    return 'I am kalyani'
app.run(debug=True,use_reloader=True)'''

#Example
from flask import Flask,request,redirect,url_for
app=Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
@app.route('/input/<name>/<place>')
def input(name,place):
    return redirect(url_for('second',user=name,city=place))
@app.route('/details')
def second():
    user=request.args.get('user')
    city=request.args.get('city')
    return f'hello,{user} you are in {city}'
app.run(debug=True,use_reloader=True)

