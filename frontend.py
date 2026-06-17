import streamlit as st
import joblib 
st.title("CGPA predictor")
st.subheader("Enter your details below")
age=st.number_input("Enter your age",19,23)
gender=st.selectbox("Gender",["Male","Female"])
screen_time=st.number_input("Enter your screen time")
social_media=st.number_input("Enter your social media hours")
online_study=st.number_input("Enter your online study time")
offline_study=st.number_input("Enter your college hours")
gaming_hours=st.number_input("Enter your gaming hours")
sleep_hours=st.number_input("Enter your sleep hours")
attendance=st.number_input("Enter your attendance %")
prev_sem_cgpa=st.number_input("Enter your previous sem CGPA")

if(gender=="Male"):
    g=1
else:
    g=0
    
model_load=joblib.load("model.pkl")


X=[[age,screen_time,social_media,online_study,gaming_hours,sleep_hours,
    attendance,offline_study,prev_sem_cgpa,g]]

result=model_load.predict(X)

button=st.button("click here to predict")

if button:
    st.write(f"### your sem cgpa is {result:.2f}")
