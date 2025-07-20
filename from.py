from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running succesfully!"

@app.route('/vamsi')
def vamsi():
    return "welcome,vamsi! This is your custom route."

if __name__ == "__main__":
    app.run(debug=True)