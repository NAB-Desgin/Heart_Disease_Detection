import joblib
import pandas as pd
import streamlit as st


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Heart AI Predictor",
    page_icon="❤️",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

body {
    background-color: #f5f7fb;
}


/* Main title */
.main-title {
    font-size: 45px;
    font-weight: 800;
    text-align: center;
    color: #d32f2f;
    margin-bottom: 5px;
}


.subtitle {
    text-align:center;
    font-size:18px;
    color:#666;
    margin-bottom:30px;
}


/* Cards */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background: white;
    border-radius:20px;
    padding:25px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.08);

}


/* Buttons */

.stButton button {

    width:100%;
    height:55px;

    background:linear-gradient(
        90deg,
        #ff416c,
        #ff4b2b
    );

    color:white;
    font-size:20px;
    font-weight:bold;

    border-radius:15px;

    border:none;

}


.stButton button:hover {

    transform:scale(1.03);

}



/* Inputs */

div[data-baseweb="input"] input {

    border-radius:10px;

}



/* Prediction */

.success-box {

    background:#d4edda;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:25px;
    color:#155724;
    font-weight:bold;

}


.danger-box {

    background:#f8d7da;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:25px;
    color:#721c24;
    font-weight:bold;

}



</style>

""", unsafe_allow_html=True)



# ---------------- HEADER ----------------


st.markdown(
    """
    <div class="main-title">
    ❤️ Heart Disease Prediction AI
    </div>

    <div class="subtitle">
    Machine Learning based cardiovascular risk analysis system
    </div>

    """,
    unsafe_allow_html=True
)



# ---------------- SIDEBAR ----------------


with st.sidebar:

    st.image(
        "heart1.jpeg",
        width=180
    )

    st.title("About")

    st.write(
        """
        This AI application predicts the possibility
        of heart disease using a trained Machine Learning model.
        
        Enter patient health parameters and get instant prediction.
        """
    )



# ---------------- LOAD MODEL ----------------


with open("log_model.joblib","rb") as file:

    model = joblib.load(file)



# ---------------- INPUTS ----------------


with st.container(border=True):


    st.subheader("🩺 Patient Information")


    col1,col2 = st.columns(2)


    with col1:


        age = st.number_input(
            "Age",
            1,
            100
        )


        gender = st.selectbox(
            "Gender",
            ["Male","Female"]
        )

        gender = 1 if gender=="Male" else 0



        chest = {
            "Typical Angina":0,
            "Atypical Angina":1,
            "Non Anginal Pain":2,
            "Asymptomatic":3
        }


        chest_pain = st.selectbox(
            "Chest Pain Type",
            chest.keys()
        )

        chest_pain = chest[chest_pain]



        bp = st.number_input(
            "Resting Blood Pressure",
            50,
            250
        )


        cholesterol = st.number_input(
            "Cholesterol",
            50,
            600
        )



        sugar = st.selectbox(
            "Fasting Blood Sugar",
            ["Yes","No"]
        )

        sugar = 1 if sugar=="Yes" else 0




    with col2:



        ecg = {

            "Normal":0,
            "ST-T Abnormality":1,
            "Left Ventricular Hypertrophy":2

        }


        restecg = st.selectbox(
            "Rest ECG",
            ecg.keys()
        )

        restecg = ecg[restecg]



        heart_rate = st.number_input(
            "Maximum Heart Rate",
            50,
            250
        )



        exercise = st.selectbox(
            "Exercise Induced Angina",
            ["Yes","No"]
        )

        exercise = 1 if exercise=="Yes" else 0



        oldpeak = st.number_input(
            "Old Peak",
            0.0,
            10.0
        )



        slope = {

            "Upsloping":0,
            "Flat":1,
            "Downsloping":2

        }


        slope_value = st.selectbox(
            "Slope",
            slope.keys()
        )

        slope_value = slope[slope_value]



        vessels = st.selectbox(
            "Major Vessels",
            [0,1,2,3]
        )



        thal = {

            "Normal":1,
            "Fixed Defect":2,
            "Reversible Defect":3

        }


        thal_value = st.selectbox(
            "Thal",
            thal.keys()
        )


        thal_value = thal[thal_value]




# ---------------- PREDICTION ----------------


st.write("")


if st.button("🔍 Predict Heart Risk"):


    data=[

        [
        age,
        gender,
        chest_pain,
        bp,
        cholesterol,
        sugar,
        restecg,
        heart_rate,
        exercise,
        oldpeak,
        slope_value,
        vessels,
        thal_value
        ]

    ]


    result=model.predict(data)[0]



    if result==0:


        st.markdown(

        """
        <div class="success-box">

        ✅ Low Risk of Heart Disease
        
        </div>

        """,

        unsafe_allow_html=True
        )


        st.image(
            "heart2.jpeg",
            width=250
        )



    else:


        st.markdown(

        """
        <div class="danger-box">

        ⚠️ High Risk of Heart Disease
        
        </div>

        """,

        unsafe_allow_html=True
        )


        st.image(
            "heart1.jpeg",
            width=250
        )