import streamlit as st

st.header("Calculate Area & Parameter :")

shape = st.selectbox("Choose", ["circle", "rectangle"])

if shape == 'circle':
    radius = st.number_input('Radius:', min_value=0.0, max_value=100.0, step=1.0)
    area = 3.14 * (radius * radius)
    parameter = 2 * (radius * radius) * 3.14
if shape == 'rectangle':
    width = st.number_input("Width", 0., step=.1)
    height = st.number_input("Height", 0., step=.1)
    area = width * height
    parameter = (2 * width) + (2 * height)

calc_btn = st.button("Compute area and parameter :")
if calc_btn:
    st.write("Area : ", area)
    st.write("Parameter : ", parameter)
