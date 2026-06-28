import streamlit as st # type: ignore

st.title("Streamlit Text Input Example")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Welcome to the Streamlit app.")