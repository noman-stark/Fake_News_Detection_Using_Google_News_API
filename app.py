from flask import Flask, render_template,request
import requests, bs4
import cosine2 as cs
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    
    claim = request.form['news']
    cs.crawler(claim)
    data = claim
    my_data = cs.detect_news(data)
  
    return render_template('result2.html', prediction = my_data)

if __name__ == '__main__':
	app.run(debug=True)