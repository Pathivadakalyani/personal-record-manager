from flask import Flask,request,render_template,url_for,redirect,session
from flask_session import Session
from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key='KS@917_PATHIVADA038'
app.config['SESSION_TYPE']='filesystem'

.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='student'
Session(app)
mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def registration():
    if request.method=="POST":
        id1=request.form['id']
        name=request.form['name']
        course=request.form['course']
        address=request.form['address']
        mobile=request.form['mobile']
        cursor=mysql.connection.cursor()
        cursor.execute('insert into students values(%s,%s,%s,%s,%s)',(id1,name,course,address,mobile))
        mysql.connection.commit()
        cursor.close()
    return render_template('registration.html')
app.run(debug=True,use_reloader=True)
