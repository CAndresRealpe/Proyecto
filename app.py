import streamlit as st

st.title("Login")

correo = st.text_input("Correo")
password = st.text_input("Contraseña", type="password")

if st.button("Ingresar"):
    st.write("Correo ingresado:", correo)
    st.write("Contraseña ingresada:", password)