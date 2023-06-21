import requests
import json

# Define the input data
data = {
    'enginesize': 2.0,
    'fuelconsumption_city': 9.5,
    'cylinders': 4
}

# Set the Content-Type header to 'application/json'
headers = {'Content-Type': 'application/json'}

# Send a POST request to the predict route
try:
    response = requests.post('http://127.0.0.1:5000/predict', json=data, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Print the predicted CO2 emission
        print(response.json()['predicted_co2'])
    else:
        # Handle other status codes
        print('Error:', response.text)

except requests.exceptions.RequestException as e:
    print('Error:', e)
