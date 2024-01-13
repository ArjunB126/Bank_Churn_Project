from flask import Flask, render_template, request
import pickle



model = pickle.load(open('Customer_Churn_Prediction.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')