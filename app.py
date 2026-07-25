# app.py - Streamlit CKD Prediction App

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Page configuration
# st.set_page_config(
#     page_title=" CKD Predictor",
#     page_icon="🩺",
# layout="wide",
# initial_sidebar_state="expanded",
# )


# . Load the trained model
model = joblib.load(filename="best_ml_model.pkl")  # Make sure your saved model is in the same folder

# . User input
st.sidebar.header("Patient Information")
Age = st.sidebar.number_input("Age (years)", min_value=1, max_value=120, value=30)
Gender = st.sidebar.selectbox("Gender", ["male", "female"])
Gender = 1 if Gender == "male" else 0
Blood_pressure = st.sidebar.number_input("Systolic BP (mmHg)", min_value=50, max_value=200, value=120)
Specific_gravity = st.sidebar.selectbox("Specific Gravity", ["1.010", "1.015", "1.020", "1.025", "1.030"])
Albumin = st.sidebar.selectbox("Albumin (0-5)", [0, 1, 2, 3, 4, 5])
Sugar = st.sidebar.selectbox("Sugar (0-5)", [0, 1, 2, 3, 4, 5])
Pus_cell = st.sidebar.selectbox("Pus Cell", ["normal", "abnormal"])
Pus_cell = 0 if Pus_cell == "abnormal" else 1
Pus_cell_clumps = st.sidebar.selectbox("Pus Cell Clumps", ["absent", "present"])
Pus_cell_clumps = 0 if Pus_cell_clumps == "absent" else 1
Bacteria = st.sidebar.selectbox("Bacteria in urine", ["absent", "present"])
Bacteria = 0 if Bacteria == "absent" else 1
Blood_glucose_random = st.sidebar.number_input("Random Blood Glucose (mg/dL)", min_value=50, max_value=500, value=100)
Blood_urea = st.sidebar.number_input("Blood Urea (mg/dL)", min_value=5, max_value=200, value=20)
Serum_creatinine = st.sidebar.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=20.0, value=1.0)
Sodium = st.sidebar.number_input("Sodium (mEq/L)", min_value=120, max_value=160, value=140)
Potassium = st.sidebar.number_input("Potassium (mEq/L)", min_value=2, max_value=10, value=4)
Hemoglobin = st.sidebar.number_input("Hemoglobin (g/dL)", min_value=5, max_value=20, value=14)
Packed_cell_volume = st.sidebar.number_input("Packed Cell Volume (%)", min_value=10, max_value=60, value=40)
White_blood_cell_count = st.sidebar.number_input("WBC Count (cells/cumm)", min_value=1000, max_value=20000, value=7000)
Red_blood_cell_count = st.sidebar.number_input("RBC Count (millions/cumm)", min_value=1, max_value=10, value=5)
Hypertension = st.sidebar.selectbox("Hypertension", ["no", "yes"])
Hypertension = 0 if Hypertension == "no" else 1

Diabetes_mellitus = st.sidebar.selectbox("Diabetes Mellitus", ["no", "yes"])
Diabetes_mellitus = 0 if Diabetes_mellitus == "no" else 1
Coronary_artery_disease = st.sidebar.selectbox("Coronary Artery Disease", ["no", "yes"])
Coronary_artery_disease = 0 if Coronary_artery_disease == "no" else 1
Appetite = st.sidebar.selectbox("Appetite", ["good", "poor"])
Appetite = 0 if Appetite == "poor" else 1
Anemia = st.sidebar.selectbox("Anemia", ["no", "yes"])
Anemia = 0 if Anemia == "no" else 1
Pedal_edema = st.sidebar.selectbox("Pedal Edema", ["no", "yes"])
Pedal_edema = 0 if Pedal_edema == "no" else 1

# . Prepare input dataframe
input_data = pd.DataFrame({
    'age': [Age],
    'gender': [Gender],
    'blood_pressure': [Blood_pressure],
    'specific_gravity': [Specific_gravity],
    'albumin': [Albumin],
    'sugar': [Sugar],
    'pus_cell': [Pus_cell],
    'pus_cell_clumps': [Pus_cell_clumps],
    'bacteria': [Bacteria],
    'blood_glucose_random': [Blood_glucose_random],
    'blood_urea': [Blood_urea],
    'serum_creatinine': [Serum_creatinine],
    'sodium': [Sodium],
    'potassium': [Potassium],
    'hemoglobin': [Hemoglobin],
    'packed_cell_volume': [Packed_cell_volume],
    'white_blood_cell_count': [White_blood_cell_count],
    'red_blood_cell_count': [Red_blood_cell_count],
    'hypertension': [Hypertension],
    'diabetes_mellitus': [Diabetes_mellitus],
    'coronary_artery_disease': [Coronary_artery_disease],
    'appetite': [Appetite],
    'anemia': [Anemia],
    'pedal_edema': [Pedal_edema]
})

###interface design
st.markdown("""
<style>

/* =========================
    Main Background
========================= */
.stApp{
    background-color:#F8FCFF;
}

/* =========================
    Sidebar Background
========================= */
section[data-testid="stSidebar"]{
    background-color:#D9F3FF;
}

/* =========================
    Sidebar Header
========================= */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color:#0077B6;
}

/* =========================
    Sidebar Text
========================= */
section[data-testid="stSidebar"] label{
    color:#1E3A5F;
font-weight:bold;
}

/* =========================
    Predict Button
========================= */

.stButton > button{
    width:100%;
    background-color:#00B4D8;
    color:white;
    border:none;
    border-radius:12px;
    padding:14px;
    font-size:18px;
    font-weight:bold;
}

.stButton > button:hover{
    background-color:#0096C7;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# 2. App layout


col1, col2 = st.columns([4,1])

with col1:

    st.markdown(f"""
    <h1 style="color:#0077B6;">
    🩺 CKD Predictor
    </h1>

    <h4 style="color:gray;">
    AI-powered Clinical Decision Support System
    </h4>
    """, unsafe_allow_html=True)

with col2:

    st.image("kidney .png", width=200)
st.divider()


## APP
#
st.write("")
col1,col2,col3 = st.columns(3)

with col1:

    st.markdown(f"""
    ### 👤 Patient Summary

    **Age:** {Age}

    **Gender:** {Gender}

    **Blood Pressure:** {Blood_pressure}

    **Blood Sugar:** {Blood_glucose_random}

    """,unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    ### 🤖 Model Information

    **Algorithm:** Random Forest

    **Accuracy:** 98.21%

    **Language:** Python

    **Framework:** Streamlit

    """,unsafe_allow_html=True) 
    
with col3:

    st.markdown(f"""
    ### ℹ  About

    This AI system predicts the likelihood of Chronic Kidney Disease using Machine Learning.

    It is designed for educational purposes.

    Always consult a healthcare professional before making medical decisions.
    
    """,unsafe_allow_html=True)
    
    


# . Prediction button
if st.button("Predict CKD"):
    # Make prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0]
    # Display results
    if prediction[0] == 1:
        st.markdown("""
        <div style="
        background:white;
        padding:25px;
        border-radius:15px;
        box-shadow:0px 2px 10px rgba(0,0,0,0.1);
        border-left:8px solid #EF4444;
        ">

        <h3 style="color:#DC2626;"> ⚠️ High Risk of Chronic Kidney Disease</h3>

        <p style="font-size:18px;">
        The patient is likely to have Chronic Kidney Disease.
        Please consult a healthcare professional.
        </p>

        <h4>Prediction Confidence: {(probability[1]*100):.2f}%</h4>

        """, unsafe_allow_html=True),
        
        st.progress(float(probability[1]))
        st.caption(f"Prediction Probability: {probability[1]*100:.2f}%")
    else:
        st.markdown(f"""

<div style="
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 2px 10px rgba(0,0,0,0.1);
border-left:8px solid #22C55E;
">

<h3 style="color:#16A34A;">✅ Low Risk of Chronic Kidney Disease</h3>

<p style="font-size:18px;">
The patient is unlikely to have Chronic Kidney Disease.
</p>

<h4>Prediction Confidence: {(probability[0]*100):.2f}%</h4>

</div>
""", unsafe_allow_html=True)
        
        st.progress(float(probability[0]))
        st.caption(f"Prediction Probability: {probability[0]*100:.2f}%")
#     # Encode categorical features (same as in training)
# mapping_gender = {"male": 1, "female": 0}
# mapping_binary = {"yes": 1, "no": 0}
# mapping_pus_cell = {"normal": 0, "abnormal": 1}
# mapping_pus_cell_clumps = {"absent": 0, "present": 1}
# mapping_bacteria = {"absent": 0, "present": 1}
# mapping_appetite = {"good": 0, "poor": 1}
    
#     # Apply mappings
# input_data['gender'] = input_data['gender'].map(mapping_gender)
# input_data['hypertension'] = input_data['hypertension'].map(mapping_binary)
# input_data['diabetes_mellitus'] = input_data['diabetes_mellitus'].map(mapping_binary)
# input_data['coronary_artery_disease'] = input_data['coronary_artery_disease'].map(mapping_binary)
# input_data['anemia'] = input_data['anemia'].map(mapping_binary)
# input_data['pedal_edema'] = input_data['pedal_edema'].map(mapping_binary)
# input_data['pus_cell'] = input_data['pus_cell'].map(mapping_pus_cell)
# input_data['pus_cell_clumps'] = input_data['pus_cell_clumps'].map(mapping_pus_cell_clumps)
# input_data['bacteria'] = input_data['bacteria'].map(mapping_bacteria)
# input_data['appetite'] = input_data['appetite'].map(mapping_appetite)
    
    
