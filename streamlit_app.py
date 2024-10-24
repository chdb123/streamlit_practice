import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

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
    #DATE,SUBSCRIBERS_GAINED,SUBSCRIBERS_LOST,VIEWS,WATCH_HOURS,LIKES,SHARES,COMMENTS,TOTAL_SUBSCRIBERS
    st.scatter_chart(data=df,X="VIEWS",Y="WATCH_HOURS",color="DATE")
