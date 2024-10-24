import streamlit as st
import pandas as pd

st.title('👉 Machine Learning Practice')

st.info('Welcome To Practice sessions   ')

st.write("Let's see the labeled data")
with st.expander("Data is"):
  df=pd.read_csv(".devcontainer /streamlit_practice.csv")
  df
  st.write("**X**")
  X = df.drop('DATE',axis=1)
  X
  st.write("**Y**")
  Y = df.DATE
  Y
