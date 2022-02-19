import numpy as np
import pickle
import pandas as pd
import streamlit as st 

mod = open('model.pkl', 'rb')
model = pickle.load(mod)

def welcome():
    return "Welcome All"

def predict_note_authentication(variance,skewness,curtosis,entropy):
     
    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

#this is main function

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:rgb(46, 125, 243);padding:10px">
    <h2 style="color:rgb(241, 153, 20);text-align:center;">WebApp for Bank Authenticator</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","")
    skewness = st.text_input("Skewness","")
    curtosis = st.text_input("Curtosis","")
    entropy = st.text_input("Entropy","")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
        st.success('The output for the given authentication is  {}'.format(result))
    if st.button("About"):
        st.text("This is a bank authentication model made using StreamLit")
        st.text("This model is built by Parthiv Akilesh A S")

if __name__=='__main__':
    main()