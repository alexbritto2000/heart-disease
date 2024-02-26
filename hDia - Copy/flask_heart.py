from flask import Flask,render_template,request,redirect
from sklearn.ensemble import RandomForestClassifier
import pickle

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bmi',methods=['POST','GET'])
def bmi():
    if request.method=="POST":
        Loc=request.form['Loc']
        d1=int(request.form['id'])
        d2=int(request.form['id'])
        return render_template('.html')

@app.route('/Predict_diabetes',methods=['POST','GET'])
def diabetes():
    if request.method=="POST":
        model=pickle.load(open('diabetes.pickle','rb'))
        Loc=request.form['Loc']
        a1=int(request.form['id'])
        a2=int(request.form['id'])
        a3=int(request.form['id'])
        a4=int(request.form['id'])
        a5=int(request.form['id'])
        a6=int(request.form['id'])
        a7=int(request.form['id'])
        print(Crp,Loc,Res)
        s=model.predict([[a1,a2,a3,a4,a5,a6,a7]])
        if s[0]==0:
            return render_template('.html')
        else:
            return redirect('/predict_diabetes')
    return render_template('.html')

@app.route('/Predict_heart',methods=['POST','GET'])
def heart():
    if request.method=="POST":
        model=pickle.load(open('heart.pickle','rb'))
        Loc=request.form['Loc']
        b1=int(request.form['id'])
        b2=int(request.form['id'])
        b3=int(request.form['id'])
        b4=int(request.form['id'])
        b5=int(request.form['id'])
        b6=int(request.form['id'])
        b7=int(request.form['id'])
        b8=int(request.form['id'])
        b9=int(request.form['id'])
        b10=int(request.form['id'])
        b11=int(request.form['id'])
        b12=int(request.form['id'])
        print(Crp,Loc,Res)
        s=model.predict([[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]])
        if s[0]==0:
            return render_template('.html')
        else:
            return redirect('/predict_heart')
    return render_template('.html')


if __name__ == "__main__":
    app.run(debug=True)
