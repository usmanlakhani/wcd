import streamlit as st 

st.title("Simple Calculator")

num1 = st.number_input('Enter 1st number', value=0.0)
num2 = st.number_input('Enter 2nd number', value=0.0)

operation = st.selectbox("Choose what you want to do with the 2 numbers entered",["+","-","*","/"])