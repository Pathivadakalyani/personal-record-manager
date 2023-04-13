from flask import Flask,flash,request,render_template,url_for,redirect,session
from flask_session import Session
from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key='KS@917_PATHIVADA038'
app.config['SESSION_TYPE']='filesystem'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='student'
Session(app)
mysql=MySQL(app)
@app.route('/')
def home():
    return render_template('eindex.html')
@app.route('/login')
def login():
    return render_template('login.html')
def home():
    return render_template('eindex.html')
@app.route('/eregistration',methods=['GET','POST'])
def registration():
    if request.method=="POST":
        eid=request.form['id']
        ename=request.form['name']
        erole=request.form['role']
        mobile=request.form['mobile']
        department=request.form['dept']
        salary=request.form['salary']
        cursor=mysql.connection.cursor()
        cursor.execute('insert into emp values(%s,%s,%s,%s,%s,%s)',(eid,ename,erole,mobile,department,salary))
        mysql.connection.commit()
        cursor.close()
        flash('Details registered Successfully')
        return redirect(url_for('login'))
    return render_template('employee.html')
app.run(debug=True,use_reloader=True)



