from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

model=pickle.load(open('models/model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/predict',method=['POST'])
def predict():
    a=request.form.get('')
    result = model.predict([[]])[0]
    return render_template('home1.html',result)

if __name__=='__main__':
    app.run(debug=True)