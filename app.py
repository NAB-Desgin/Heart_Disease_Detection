import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_icon="",page_title="Heart Disease Prediction",layout="wide")

with st.sidebar:
    st.title("Heart Disease Prediction")

df=pd.read_csv("cleaned_data.csv")
with open("log_model.joblib","rb")as file:
    model=joblib.load(file)

with st.container(border=True):
    col1,col2=st.columns(2)
    with col1:
        age=st.number_input("AGE",min_value=1,max_value=100,step=5)
        gender=st.radio("GENDER", options=['Male','Female'],horizontal=True)
        gender=1 if gender=='Male' else 0
        d={"Typical angina":0,"Atypical angina":1,"non-anginal pain":2,"Asympototic":3}
        chest_pain_type=st.selectbox("CHEST PAIN TYPE", options=d.keys())
        chest_pain_type=d[chest_pain_type]
        resting_bp=st.number_input("RESTING BP",min_value=50,max_value=250,step=10)
        cholestrol=st.number_input("CHOLESTROL",min_value=50,max_value=600,step=20)
        fbs=st.radio("FASTING BLOOD SUGAR", options=['Yes','No'],horizontal=True)
        fbs=1 if fbs=='Yes' else 0

    with col2:
        d2={"normal":0,"having ST-T":1,"left Ventricular hypertrophy":2}
        restecg=st.selectbox("RESTING ECG", options=d2.keys())
        restecg=d2[restecg]
        max_heart=st.number_input("MAXIMUM HEART RATE",min_value=50,max_value=250,step=5)
        exang=st.radio("EXERCISE INDUECD ANGINA", options=['Yes','No'],horizontal=True)
        exang=1 if exang=='Yes' else 0
        old_peek=st.number_input("OLDPEEK",min_value=0.0,max_value=10.0,step=1.0)
        d3={"upsloping":0,"flat":1,"downsloping":2}
        slope=st.selectbox("SLOPE", options=d3.keys())
        slope=d3[slope]
        num_vessles=st.selectbox("NUMBER OF MAJOR VESSELS", options=[0,1,2,3])
        d4={"normal":1,"fixed Defect":2,"reversable defect":3}
        thal=st.selectbox("THAL", options=d4.keys())
        thal=d4[thal]

if st.button("PREDICT"):
    data=[[age,gender,chest_pain_type,resting_bp,cholestrol,fbs,restecg,max_heart,exang,old_peek,slope,num_vessles,thal]]
    pred=model.predict(data)[0]

    if(pred==0):
        st.subheader("Low Risk of Heart Disease")
        st.image("heart2.jpeg",width=200)

    else:
        st.subheader("High Risk of Heart Disease")
        st.image("heart1.jpeg",width=200)    




   




