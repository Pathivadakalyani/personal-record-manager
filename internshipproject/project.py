'''from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return 'welcome to application'
@app.route('/homepage',methods=['GET','POST'])
def home():
    if request.method=='POST':
       user=request.form['name']
       python=request.form['python']
       mysql=request.form['mysql']
       html=request.form['html']
       return f'enterd data is {user} {python} {mysql} {html}'
    else:
        return render_template('index.html')
app.run() '''

#jinja2 example
from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return 'welcome to application'
@app.route('/homepage',methods=['GET','POST'])
def home():
    if request.method=='POST':
       user=request.form['name']
       python=int(request.form['python'])
       mysql=int(request.form['mysql'])
       html=int(request.form['html'])
       return render_template('indexs.html',user=user,python=python,mysql=mysql,html=html)
    else:
       return render_template('index.html')
app.run(use_reloader=True)   


