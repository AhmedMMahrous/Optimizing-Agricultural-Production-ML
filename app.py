import numpy as np
import pandas as pd
import joblib
from flask import Flask,render_template,request


app = Flask(__name__)

model = joblib.load('Optimizing Agricultural Production.save')

# Home
@app.route('/')
def home():
    return render_template('Home.html')

# Analysis
@app.route('/analysis', methods=['GET'])
def analysis():
    return render_template('Analysis.html')


# About me
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

# predict
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Ratio_of_Nitrogen_content_in_soil = request.form['Ratio_of_Nitrogen_content_in_soil']
        Ratio_of_Phosphorous_content_in_soil = request.form['Ratio_of_Phosphorous_content_in_soil']
        Ration_of_Potassium_content_in_soil = request.form['Ration_of_Potassium_content_in_soil']
        Temperature_in_degree_Celsius = request.form['Temperature_in_degree_Celsius']
        Relative_humidity = request.form['Relative_humidity']
        ph_value_of_the_soil = request.form['ph_value_of_the_soil']
        Rainfall_in_mm = request.form['Rainfall_in_mm']

        List = [Ratio_of_Nitrogen_content_in_soil,
                Ratio_of_Phosphorous_content_in_soil,
                Ration_of_Potassium_content_in_soil,
                Temperature_in_degree_Celsius,
                Relative_humidity,
                ph_value_of_the_soil,
                Rainfall_in_mm]
        inp_data = [(float(x)) for x in List]

        prediction = model.predict([inp_data])
        prediction = (prediction[0])
        return render_template('Predict.html', pred_val=prediction)
    else:
        return render_template('Predict.html')



# The Function called when the scipt is run
if __name__ == '__main__':
    app.run(debug=True)