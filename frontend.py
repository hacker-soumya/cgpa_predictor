import streamlit as st
import joblib 
st.title("CGPA predictor")
st.subheader("Enter your details below")

age=st.slider("Enter your age",19,23)

gender=st.radio("Select your gender",["Male","Female"])

screen_time=st.number_input("Enter your screen time",0,10)

study_hours=st.number_input("Enter your study hours",2,10)

sleep_hours=st.number_input("Enter your sleep hours",5,8)

attendance=st.number_input("Enter your attendance %",max_value=100)

prev_sem_cgpa=st.number_input("Enter your previous sem CGPA",max_value=10)


if(gender=="Male"):
    g=1
else:
    g=0
    
model_load=joblib.load("model.pkl")

X=[[age,gender,study_hours,sleep_hours,attendance,prev_sem_cgpa,screen_time]]
 
result_array=model_load.predict(X)

result=result_array.item()

button=st.button("click here to predict")

if button:
    st.write(f"### your sem cgpa is {result:.2f}")
