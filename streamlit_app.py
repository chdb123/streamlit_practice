import streamlit as st
import pandas as pd

st.title('👉 Machine Learning Practice')

st.info('Welcome to Practice sessions')

st.write("Let's see the labeled data")

# Load and display data
with st.expander("Data is"):
  df=pd.read_csv(".devcontainer /streamlit_practice.csv")
  df
  st.write("**X**")
  X = df.drop('Date',axis=1)
  X
  st.write("**Y**")
  Y = df.Date
  Y

with st.expander("Data Visualization:"):
    # Create a new DataFrame with only the columns required for plotting
    chart_data = df[['VIEWS', 'WATCH_HOURS']]
    
    # Plot the scatter chart
    st.write("Scatter plot of VIEWS vs WATCH HOURS")
    st.scatter_chart(chart_data)
