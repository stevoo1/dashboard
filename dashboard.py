import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    st.subheader("Basic Info")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        column = st.selectbox("Choose column for histogram", numeric_cols)
        fig, ax = plt.subplots()
        ax.hist(df[column], bins=20)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns found for chart")

else:
    st.info("Upload a CSV file to begin analysis")