import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('xgb_1.pkl','rb'))


@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')
    #return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():

    #Extract input from form
    joblevel=request.form.get("JobLevel")
    stockoption=request.form.get("StockOptionLevel")
    yearswithmanager=request.form.get("YearsWithCurrManager")
    monthlyincome=request.form.get("MonthlyIncome")
    totalworking=request.form.get("TotalWorkingYears")
    yearssincelast=request.form.get("YearsSinceLastPromotion")
    yearsincurrentrole=request.form.get("YearsInCurrentRole")
    yearsatcompany=request.form.get("YearsAtCompany")
    
    #Create the Dataframe based on input
    
    input_variables=pd.DataFrame([[joblevel,stockoption,yearswithmanager,monthlyincome,totalworking,yearssincelast,yearsincurrentrole,yearsatcompany]],
                                    columns=['JobLevel','StockOptionLevel','YearsWithCurrManager','MonthlyIncome','TotalWorkingYears','YearsSinceLastPromotion','YearsInCurrentRole','YearsAtCompany'],
                                    dtype=float,
                                    index=['input'])
                                    
                                    
    prediction=model.predict(input_variables)[0]
     
     
    
    
    #int_features = np.array[float(x) for x in request.form.values()]
    #final_features = np.array(int_features)
    #prediction = model.predict(int_features.T)
    #print(prediction[0])

    #output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="Attrition {}".format(prediction))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)



if __name__ == '__main__':
    app.run(debug=True)