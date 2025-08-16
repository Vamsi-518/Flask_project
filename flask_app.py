from flask import 

app = Flask(__name__ )    

@app.route('/')
def index():
    return render_template('33333.html')

@app.route('/submit',methods =['post'])
def submit():   
    name = request.form.get ('name')
    return render_template('result.html',name=name)

if __name__=='__main__':
    app.run(debug=True) 