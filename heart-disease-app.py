import streamlit as st
from joblib import load
import tensorflow as tf

# Let's define helper functions
def create_header():
  st.title("Inspirit AI: Heart Disease Model")
  st.header("By InspiritAI")
  st.subheader("Given your blood pressure and heart rate, let's predict if you have heart disease!")

def get_user_input():
  blood_pressure = st.number_input("What is your blood pressure?")
  heart_rate = st.number_input("What is your maximum heart rate during exercise in beats per minute?")
  input_features = [[blood_pressure, heart_rate]]
  return input_features

def make_prediction(model, input):
  return model.predict(input)

def get_app_response(prediction):
  if prediction == 1:
    st.write("The model predicts you have heart disease.")
  elif prediction == 0:
    st.write("The model predicts you do not have heart disease.")
  else:
    st.write ("No results yet")

# Load our DecisionTree model into our web app
model = load("heart-disease-model.joblib")
st.write ("Model uploaded!") # You may remove this in your finalized web app!

create_header()
input_features = get_user_input()
prediction = make_prediction(model, input_features)
get_app_response(prediction)
