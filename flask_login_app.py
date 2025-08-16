from flask import Flask, render_template, request, redirect, url_for, flash, session
 
app = Flask(__name__)
app.secret_key = 'your_secret_key'

USER = {
    "username": "admin",
    "password": "1234"
}

@app.route('/')
def home():
    if 'username' in session:
        return f"Welcome {session['username']}! <a href='/logout'>Logout</a>"
    return redirect(url_for('login')) 

@app.route('/login', methods=['GET', 'POST'])
def login():   
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USER['username'] and password == USER['password']:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or pass word')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(debug=True)                                                      