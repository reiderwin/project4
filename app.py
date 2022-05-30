# from crypt import methods
from pydoc import allmethods
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

from flask import Flask, jsonify, render_template, request 

#################################################
# Database Setup
#################################################
SERVER = '127.0.0.1'
DATABASE = 'project4'
USERNAME = 'postgres'
PASSWORD_2 = 'Butt'
DATABASE_CONN = f'postgresql://{USERNAME}:{PASSWORD_2}@{SERVER}/{DATABASE}'
engine = create_engine(DATABASE_CONN)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
session = Session(engine)
results = engine.execute("SELECT * FROM loan_data").fetchall()
session.close()


# create route that renders index.html template
@app.route("/")
def index():

    return render_template("index.html") 

@app.route("/formurl", methods=["post"])
def get_values():

    # Get input values for the model from html
    input = []
    loan_amount = request.form["loanamount"] # for the input
    input.append(loan_amount)
    income = request.form["income"]
    input.append(income)
    loantype = request.form["type"]
    for i in loantype:
        input.append(i)
    aeth = request.form["aeth"]
    for i in aeth:
        input.append(i)
    coaeth = request.form["coaeth"]
    for i in coaeth:    
        input.append(i)
    arac = request.form["arac"]
    for i in arac:
        input.append(i)
    coarac = request.form["coarac"]
    for i in coarac:
        input.append(i)
    asex = request.form["asex"]
    for i in asex:
        input.append(i)
    coasex = request.form["coasex"]
    for i in coasex:
        input.append(i)

    print("---------------------------------------------")
    print(input)
    print("---------------------------------------------")

    import pickle


    model = pickle.load(open('Resources/lr_classifier.pkl', 'rb'))       
    chance=0

    data = np.array(input)[np.newaxis, :]  # converts shape for model test
    predict = model.predict(data)  # runs model on the data
    prob= model.predict_proba(data)


    if predict == [1]:
        prediction = "We predict success, congratulations!"
    else:
        prediction = "Sorry, you will likely not qualify."

    prob= model.predict_proba(data)

    if predict == [1]:
        chance = prob[0][1]
    else:
        chance = prob[0][0]

    print(prediction)
    print("---------")
    print(chance)

            
    model_result = {
        "prediction":prediction,
        "probability":str((chance*100)) + '%'
    }
    # Load he model and feed the input to the model to get the result
    # model_result = michales_fantastic_model_result

    # Render the result through a html page
    return render_template("result.html", result = model_result) 
    #return render_template("index.html",)    

@app.route("/loandata/api")
def data_crops():
    loan_data = []
    for id, loan_type , loan_amount_000, action_taken, applicant_ethnicity, co_applicant_ethnicity, applicant_race_1, co_applicatn_race_1, applicant_sex, co_applicant_sex, applicant_income, purchaser_type in results:
        loans = {}
        loans["id"] = id
        loans["loan_type"] = loan_type
        loans["loan_amount_000's"] = loan_amount_000
        loans["action_taken"] = action_taken
        loans["applicant_ethnicity"] = applicant_ethnicity
        loans["co_applicant_ethnicity"] = co_applicant_ethnicity
        loans["applicant_race_1"] = applicant_race_1
        loans["co_applicant_race_1"] = co_applicatn_race_1
        loans["applicant_sex"] = applicant_sex
        loans["co_applicant_sex"] = co_applicant_sex
        loans["applicant_income_000's"] = applicant_income
        loans["purchaser_type"] = purchaser_type
        
        loan_data.append(loans)


    return jsonify(loan_data)

if __name__ == '__main__':
    app.run(debug=True)