from flask import Flask, redirect, render_template,request,url_for,jsonify
from datetime import *
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)

        if username == 'admin' and password == 'superduperroot':
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid credentials")
    
    return render_template('login.html')

@app.route("/index")
def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)