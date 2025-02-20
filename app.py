import streamlit as st 

st.title("Personal Profile Manager")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", 0, 120, 25)
bio = st.text_area("Write a short bio")

hobbies = st.multiselect(
    "Select your hobbies",
    ["Reading", "Gaming", "Sports", "Cooking", "Travel"]
)

if st.button("Show My Profile"):
    st.markdown(f""" # Profile Information
    **Name:** {name},
    **Age:** {age},   
    **Bio:**
    {bio}
    """)