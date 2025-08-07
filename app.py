## Building Web app of House Price Prediction

# Import the Streamlit library for building web apps
import streamlit as st

# Import NumPy for numerical operations (used for array conversion)
import numpy as np

# Import joblib for loading the pre-trained machine learning model
import joblib

# Load the pre-trained model from the specified file path
model = joblib.load('machine_learning_Project\IIndProject.py\model.pkl')  # Load the pre-trained model

# Set the title of the Streamlit app
st.title('House Price Prediction App')

# Add a horizontal divider for visual separation
st.divider()

# Display a description of the app and instructions for the user
st.write("This app uses machine learning for prediction house price with given features of the house. For usingthis app you can enter the inputs from this user interface and then use Predict Button ")

# Add another divider for clarity
st.divider()

# Create a number input widget for the number of bedrooms (default 0)
bedrooms = st.number_input('Number of bedrooms', min_value=0, value=0)

# Create a number input widget for the number of bathrooms (default 0)
bathrooms = st.number_input('Number of bathrooms', min_value=0, value=0)

# Create a number input widget for the living area (default 2000)
livingarea = st.number_input('Living area ', min_value=0, value=2000 )

# Create a number input widget for the condition of the house (default 3)
condition = st.number_input('Condition', min_value=0, value=3)

# Create a number input widget for the number of nearby schools (default 0)
numberofschools = st.number_input('Number of schools nearby', min_value=0, value=0)

# Add another divider for separation
st.divider()

# Combine all input values into a 2D list (required format for model prediction)
x = [[bedrooms, bathrooms, livingarea, condition, numberofschools]]

# Add a button labeled 'Predict' for triggering the prediction
predictbutton = st.button('Predict')

# If the 'Predict' button is pressed:
if predictbutton:
    # Show a balloon animation for user feedback
    st.balloons()
    # Convert the input list to a NumPy array for the model
    x_array = np.array(x)
    # Use the loaded model to predict the house price (take the first result)
    prediction = model.predict(x_array)[0]
    # Display the predicted price, formatted with commas and two decimals
    st.write(f"Price Prediction is {prediction:,.2f}")
else:
    # If the button is not pressed, prompt the user to use it

    st.write('Please use predict button after entering values.')
