import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('logistic_regression_model.joblib')

# Define the prediction function
def predict_diabetes(Age, Weight, Height, Poverty, HomeRooms, SmokeNow):
    # Create a DataFrame from the input features
    input_data = pd.DataFrame({
        'Age': [Age],
        'Weight': [Weight],
        'Height': [Height],
        'Poverty': [Poverty],
        'HomeRooms': [HomeRooms],
        'SmokeNow': [SmokeNow]
    })

    # Make the prediction using the loaded model
    prediction = model.predict(input_data)

    # Return the predicted class
    return 'Diabetic' if prediction[0] == 0 else 'Non-Diabetic'

st.image("engage_jooust_branding.png",caption="Engage brands")
st.markdown("[ENGAGE program](https://engage.uonbi.ac.ke)")
# Streamlit app
st.title('Diabetes Prediction App')

# Input fields for user data
Age = st.number_input('Age', min_value=0, max_value=100, step=1)
Weight = st.number_input('Weight (in kg)')
Height = st.number_input('Height (in cm)')
Poverty = st.selectbox('Poverty Level (0-1)', [0, 1])
HomeRooms = st.number_input('Number of Rooms in Home', min_value=0, max_value=7, step=1)
SmokeNow = st.selectbox('Do you currently smoke?', ['No', 'Yes'])

# Map 'Yes' to 1 and 'No' to 0 for SmokeNow
SmokeNow = 1 if SmokeNow == 'Yes' else 0

# Prediction button
if st.button('Predict'):
    result = predict_diabetes(Age, Weight, Height, Poverty, HomeRooms, SmokeNow)
    st.success(f'Prediction: {result}')
