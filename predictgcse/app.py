# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:57:48 2017

@author: Home
"""

from flask import Flask, request, render_template, jsonify #, redirect, url_for
import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
#import psycopg2

app = Flask(__name__)

@app.route('/')
def upload_data():
    return render_template('uploaddata.html')

@app.route('/home') #retrieve uploaded file and let user select features
#for prediction from it
def home():
    return render_template('home.html') 
  
@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify({'prediction': list(prediction)})
if __name__ == '__main__':
     clf = joblib.load('webmodel.pkl')
     app.run( )

 
