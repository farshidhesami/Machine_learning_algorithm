import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the dataset from a CSV file
df = pd.read_csv('FuelConsumption2023.csv', encoding='latin-1')

# Select specific columns of interest
df = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'CO2EMISSIONS']]

# Data preprocessing
df.dropna(inplace=True)
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Train the model
model = LinearRegression()
X = df_scaled[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY']]
y = df_scaled['CO2EMISSIONS']
model.fit(X, y)

# Save the trained model
# We can uncomment the following line to save the model if needed
# model.save('co2_emission_model.pkl')