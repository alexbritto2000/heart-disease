from flask import Flask,render_template,url_for,request,redirect,session
import pickle
from sklearn.ensemble import RandomForestClassifier
import sqlite3 as sql

app = Flask(__name__)
con=sql.connect('heartdb.db')
con.execute('create table if not exists register(uname varchar(30),email varchar(30),password varchar(30))')

@app.route('/')
def home():
        return render_template('index.html')

@app.route('/login.html')
def login_1():
        return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
        print('hi')
        if request.method=='POST':
                name=request.form['uname']
                pa=request.form['upassword']
                con=sql.connect('heartdb.db')
                cur=con.cursor()
                cur.execute('select password from register where uname=?',(name,))
                a=cur.fetchone()
                print(a)
                if a is not None and len(a) > 0 and a[0] == pa:
                # Unna vendru vela panna kodukkum kooda irukkum
                        return render_template('BMI.html')
                else:
                        return render_template('login.html')
        return render_template('login.html')


@app.route('/register.html')
def register_1():
        return render_template('register.html')


@app.route('/register',methods=['POST','GET'])
def register():
        if request.method=='POST':
                uname=request.form['uname']
                email=request.form['uemail']
                password=request.form['upassword']
                password1=request.form['upassword1']
                if password==password1:
                        with sql.connect('heartdb.db') as con:
                                cur=con.cursor()
                                cur.execute('insert into register(uname,email,password) values(?,?,?)',(uname,email,password))
                                con.commit()
                                print("Data saved successfully")
                                return render_template('login.html')
                else:
                        return render_template('register.html')
        return render_template('register.html')

@app.route('/BMI.html')
def bmi1():
	return render_template('BMI.html')

@app.route('/bmivalue',methods=['POST','GET'])
def bmi():
        if request.method=="POST":
                c1=float(request.form['30'])
                c2=int(request.form['31'])
                c3=round(c2 / (c1 * c1), 2)
                c3=str(c3)
                return render_template('bmiresult.html',c=c3)
        return render_template('BMI.html')

@app.route('/Diabetes')
def dia():
        return render_template('Diabetes.html')

@app.route('/Diabetes.html',methods=['POST','GET'])
def diabetes():
        if request.method=="POST":
                model=pickle.load(open('diabetesnew.pickle','rb'))
                a1=float(request.form['1'])
                a2=float(request.form['2'])
                a3=float(request.form['3'])
                a4=float(request.form['4'])
                a5=float(request.form['5'])
                a6=float(request.form['6'])
                a7=float(request.form['7'])
                s=model.predict([[a1,a2,a3,a4,a5,a6,a7]])
                if s[0]==0:
                        return render_template('Diabetes__Not_Predicetd.html')
                else:
                        return render_template('Diabetes_Predicetd.html')
                return render_template('Diabetes1.html')

@app.route('/Heart.html',methods=['POST','GET'])
def heart():

    return render_template('Heart.html')

@app.route('/heartresult',methods=['POST','GET'])
def heart1():
        if request.method=="POST":
                model=pickle.load(open('heartnew.pickle','rb'))
                dict1={'Female':1,'Male':0,'female':1,'male':0,'FEMALE':1,'MALE':0,'yes':1,'no':0,'YES':1,'NO':0,'YES':1,'No':0}
                b1=request.form['11']
                b1=dict1[b1]
                b2=float(request.form['21'])
                b3=request.form['31']
                b3=dict1[b3]
                b4=float(request.form['41'])
                b6=request.form['61']
                b6=dict1[b6]
                b7=float(request.form['71'])
                b8=request.form['81']
                b8=dict1[b8]
                b9=float(request.form['91'])
                b10=float(request.form['10'])
                b11=float(request.form['011'])
                b12=float(request.form['12'])
                b13=float(request.form['13'])
                d=model.predict([[b1,b2,b3,b4,b6,b7,b8,b9,b10,b11,b12,b13]])
                if d[0]==0:
                        return render_template('heart_disease_not.html')
                else:
                        return render_template('heart_disease.html')
                return render_template('Diabetes.html')


@app.route('/Doctors.html')
def doctors():
    return render_template('Doctors.html')


@app.route('/bmiresult.html')
def bmir():
    return render_template('bmiresult.html')


if __name__ == '__main__':
        
        app.run(debug=True)
