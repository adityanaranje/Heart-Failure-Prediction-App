# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:00:26 2021

@author: ADITYA NARANJE
"""

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("heart_p.html")

#prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,12)
    loaded_model = pickle.load(open("heart_flask.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

#Output page
@app.route('/result', methods = ["POST"])
def result():
    if request.method =="POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int,to_predict_list))
        result = ValuePredictor(to_predict_list)
        if int(result)==0:
            pred = "No Chance of Heart Failure"
        else:
            pred = "Chance of Heart Failure"
        return render_template("heart_result.html",prediction=pred)
    
#Main function
if __name__=="__main__":
    app.run(debug=True)
    app.config["TEMPLATES_AUTO_RELODE"]=True