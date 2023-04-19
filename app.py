from numpy import right_shift
import streamlit as st
import time
from streamlit.elements.button import ButtonMixin
from sympy import ceiling

st.title(":green[A.Z.B] :red[Serveys]")

st.latex("Please Answer the following Questions")

st.write("First of all, Play the music to relieve your stress")

st.audio("/content/Relax-cut2.mp3")

st.latex("General Info")

placeholder2 = st.empty()
placeholder3 = st.empty()
placeholder4 = st.empty()
placeholder5 = st.empty()
placeholder6 = st.empty()
placeholder7 = st.empty()
placeholder8 = st.empty()

Fname = placeholder2.text_input("First name", key="3")
Lname = placeholder3.text_input("Last name", key="4")
add = placeholder4.text_input("Full Address", key="5")
email = placeholder5.text_input("Email Address", key="6")
description = placeholder6.text_input("Describe yourself in no more than 10 sentences", key="7")
phone = placeholder7.text_input("Phone Number", key="8")
age = placeholder8.slider("Age", 10,100, key="20")
gender = st.radio("Gemder", ("Male", "Female"))

st.text("Do You Love Your Family ?")
if st.checkbox("Yes🥺"):
    Love = True
if st.checkbox("No🥲"):
    love = False

Sure = False
st.write("* Please review your Information Last time Crefully before sending it")  
st.write("* Are you sure that the information you provided is right, you will not be able to change it later⚠️")
if st.checkbox("Yes"):
    Sure = True
if st.checkbox("No"):
    Sure = False

placeholder = st.empty()

if(placeholder.button('Submit', disabled=False, key="1")):
    if(Sure):
      placeholder.button("Submit", disabled=True, key="2")
      placeholder2.text_input("First name", key="9", disabled=True)
      placeholder3.text_input("Last name", key="10", disabled=True)
      placeholder4.text_input("Full Address", key="11", disabled=True)
      placeholder5.text_input("Email Address", key="12", disabled=True)
      placeholder6.text_input("Describe yourself in no more than 10 sentences", key="13", disabled=True)
      placeholder7.text_input("Phone Number", key="14", disabled=True)
      placeholder8.slider("Age", 10,100, key="22", disabled=True)
      with st.spinner('Saving Information'):
        time.sleep(5)
        st.success('Your Response has been saved successfully')
      st.header("Your information")  
      st.write("Fname: ", Fname)
      st.write("Lname: ", Lname)
      st.write("Age: ", age)
      st.write("Full Address: ", add)
      st.write("Email: ", email)
      st.write("Phone Number: ", phone) 

      st.header("Thank you for taking this servey")      
    else:
      st.text("Please Review your information.")  