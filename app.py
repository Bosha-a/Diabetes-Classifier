import streamlit as st 
import numpy as np 
import pickle as pkl


model = 'model.pkl'
with open(model, 'rb') as f:
    loaded_model = pkl.load(f)


# pregnancies = st.number_input('Pregnancies')
glucose= st.number_input('Glucose')
# blood_pressure =  st.number_input('BloodPressure')
# skin_thickness = st.number_input('SkinThickness')
# insulin = st.number_input('Insulin')
bmi = st.number_input('BMI')
# diabetes_pedigree_function = st.number_input('DiabetesPedigreeFunction')
# age = st.number_input('Age')

# input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
input_data = np.array([[glucose , bmi]])

if st.button("Predict"):
    prediction = loaded_model.predict(input_data)
    
    if prediction[0] == 1:
        st.write("You have diabetes.")
    else:
        st.write("You don't have diabetes.")
