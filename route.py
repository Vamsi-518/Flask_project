from flask import Flask

app = Flask(__name__)


def vamsi():
    return 'this is python'
app.add_url_rule('/vamsi','vamsi',vamsi)

if __name__ == '__main__':
    app.run(debug=True)