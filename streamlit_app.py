import streamlit as st
import pandas as pd

st.title('👉 Machine Learning Practice')

st.info('Welcome to Practice sessions')

st.subheading("Let's see the labeled data")

# Load and display data
with st.expander("Data is"):
  df=pd.read_csv(".devcontainer /streamlit_practice.csv")
  df
  st.write("**X**")
  X = df.drop('DATE',axis=1)
  X
  st.write("**Y**")
  Y = df.DATE
  Y

with st.expander("Data Visualization:"):
    # Create a new DataFrame with only the columns required for plotting
    df.set_index('DATE', inplace=True)
    chart_data = df[['VIEWS', 'WATCH_HOURS']]
    chart_data
    
    st.write("Bar graph of VIEWS vs WATCH HOURS")
    st.bar_chart(chart_data)
