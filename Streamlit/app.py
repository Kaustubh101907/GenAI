import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

## Title of the application
st.title("My Streamlit Application")

## display a simple text
st.write("Welcome to my Streamlit app! This is a simple demonstration of how to use Streamlit to create interactive web applications with Python.")

## create a simple dataframe
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': ['A', 'B', 'C', 'D', 'E']
})

## display the dataframe
st.write("Here is a simple dataframe:")
st.dataframe(df)

## create a simple line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)