import streamlit as st
import pandas as pd

st.title('👉 Machine Learning Practice')

st.info('Welcome to Practice sessions')

st.write("Let's see the labeled data")

# Load and display data
with st.expander("Data is"):
    # Adjust the file path according to your setup
    df = pd.read_csv(".devcontainer/streamlit_practice.csv")
    st.write("**Full Data**")
    st.dataframe(df)
    
    # Separate features (X) and target (Y)
    st.write("**X (Features)**")
    X = df.drop('DATE', axis=1)
    st.dataframe(X)
    
    st.write("**Y (Target)**")
    Y = df['DATE']
    st.dataframe(Y)

with st.expander("Data Visualization:"):
    # Create a new DataFrame with only the columns required for plotting
    chart_data = df[['VIEWS', 'WATCH_HOURS']]
    
    # Plot the scatter chart
    st.write("Scatter plot of VIEWS vs WATCH HOURS")
    st.scatter_chart(chart_data)
