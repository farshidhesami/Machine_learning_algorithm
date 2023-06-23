import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from flask import Flask, render_template, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Load the dataset from a CSV file
df = pd.read_csv('FuelConsumption2023.csv', encoding='latin-1')

# Select specific columns of interest
df = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'CO2EMISSIONS']]

# Data preprocessing
df.dropna(inplace=True)
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Define route to handle the root URL
@app.route('/')
def home():
    return render_template('home.html')

# Define route to handle the predict URL
@app.route('/predict', methods=['POST'])
def predict():
    try:
        enginesize = float(request.form['enginesize'])
        fuelconsumption_city = float(request.form['fuelconsumption_city'])
        cylinders = int(request.form['cylinders'])

        # Create the input data
        input_data = pd.DataFrame([[enginesize, cylinders, fuelconsumption_city]], columns=['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY'])

        # Scale the input data
        input_data_scaled = pd.DataFrame(scaler.transform(input_data), columns=input_data.columns)

        # Predict CO2 emission
        predictions = model.predict(input_data_scaled)

        # Inverse transform the predicted values
        predicted_co2 = scaler.inverse_transform(predictions)[0]

        return render_template('index.html', predicted_co2=predicted_co2)

    except Exception as e:
        error = str(e)
        return render_template('index.html', error=error)

if __name__ == '__main__':
    
    # Load the pre-trained model
    model = LinearRegression()
    X = df_scaled[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY']]
    y = df_scaled['CO2EMISSIONS']
    model.fit(X, y)


    # Run the Flask application
    app.run(debug=True)
