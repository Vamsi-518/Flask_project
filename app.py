from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == "admin" and password == "1234":
        return render_template('welcome.html', name=username)
    else:
        return "Invalid Credentials. Try again."

if __name__ == '__main__':
    app.run(debug=True)
