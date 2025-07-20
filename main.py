from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to the Home Page</h1>'

@app.route('/home')
def home():
    return '<h1>This is the Home page</h1>'

@app.route('/user/about')
def about():
    return '<h1>About the User</h1>'

if __name__=='__main__':
    app.run(debug=True)