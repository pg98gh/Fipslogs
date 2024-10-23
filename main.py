from flask import Flask, redirect, render_template,request,url_for,jsonify
from datetime import *
app = Flask(__name__)

@app.route("/")
def start():
    return render_template("login.html")

@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password = request.form['password']
        print(username,password)
        if username == 'admin' and password == 'superduperroot':
            return redirect(url_for('index'))
        else:
            return render_template('login.html')
    #return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route("/index")
def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)