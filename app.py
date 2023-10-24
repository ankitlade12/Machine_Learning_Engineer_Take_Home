import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

# Load your trained LSTM model
model = load_model('final_model.h5')  # Replace with the path to your model file.

# Load and preprocess your 2021 data
data_2021 = pd.read_csv('data_daily.csv')  # Replace '2021_receipts_data.csv' with your data file.
data_2021['# Date'] = pd.to_datetime(data_2021['# Date'])
data_2021.set_index('# Date', inplace=True)
monthly_data_2021 = data_2021['Receipt_Count'].resample('M').sum()
#monthly_data_2021_m = data_2021['Receipt_Count'].resample('M').sum()
scaler = MinMaxScaler()
normalized_data_2021 = scaler.fit_transform(monthly_data_2021.values.reshape(-1, 1))

# Corrected sequence length
seq_length = 1

# Initialize a list to store the simulated 2022 data
simulated_data_2022 = list(normalized_data_2021[-seq_length:])

# Create a function to generate monthly predictions
def generate_monthly_predictions(model, current_seq):
    # Predict the next month
    predicted_value = model.predict(current_seq)
    return predicted_value[0][0]

# Loop over each month in 2022
for _ in range(12):
    # Create the current sequence for prediction
    current_seq = np.array([simulated_data_2022[-seq_length:]]).reshape(1, seq_length, 1)
    
    # Generate the prediction for the month
    predicted_value = generate_monthly_predictions(model, current_seq)
    
    # Append the predicted value to the simulated data
    simulated_data_2022.append([predicted_value])

# Inverse transform the simulated data to the original scale
simulated_data_2022 = scaler.inverse_transform(np.array(simulated_data_2022).reshape(-1, 1))

# Create a Streamlit app
st.title("Scanned Receipts Prediction for 2022")

# Display the simulated monthly data for 2022
st.write("Simulated Monthly Scanned Receipts for 2022:")

# Create a dropdown to select the month of 2022
selected_month = st.selectbox("Select a month of 2022", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Find the index of the selected month
months_2022 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
selected_index = months_2022.index(selected_month)

# Display the prediction for the selected month
st.write(f"Predicted Scanned Receipts for {selected_month} 2022: {int(simulated_data_2022[selected_index][0])}")

# Data for the selected month of 2022 and the entire 2021 data
selected_data_2022 = simulated_data_2022[selected_index]
entire_2021_data = monthly_data_2021

# Create a line graph that combines 2021 and 2022 data
plt.figure(figsize=(10, 6))
x_values_2021 = list(range(1, 13))  # Numeric values for months from 1 to 12
y_values_2021 = entire_2021_data.values
x_values_2022 = [13]  # Numeric value for the selected month in 2022 (e.g., January 2022)
y_values_2022 = [selected_data_2022]

plt.plot(x_values_2021, y_values_2021, label='2021 Data', marker='o', markersize=5)
plt.plot(x_values_2022, y_values_2022, label=f'{selected_month} 2022 Data (Predicted)', marker='s', markersize=5)

plt.title(f"Scanned Receipts for {selected_month} 2022 and 2021")
plt.xlabel("Month")
plt.ylabel("Receipts")
plt.xticks(list(range(1, 14)), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', f'{selected_month}'])
plt.legend()
st.pyplot()








    

