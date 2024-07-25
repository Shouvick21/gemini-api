
import google.generativeai as genai
import os
import streamlit as st


st.title("welcome to ai generator")
st.write("hello! please write your name")
name=st.text_input("please enter your name")
btn=st.button("submit")




apikey="AIzaSyD_vUrHrZNw_BhY8uu9210y-D3BLYDp-RI"
genai.configure(api_key=apikey)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content(f"{name}")
print(response.text)
if btn and name:
    st.text_area("Name",f"{response.text}")