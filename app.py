import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load(r"model/best_svm_model.pkl")
top_20_features = joblib.load(r"model/top_20_features.pkl")

st.title("Gene Expression Prediction App")
st.markdown("Upload your gene data (CSV with gene_0 to gene_2000)")


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)


    if 'Unnamed: 0' in data.columns:
        data = data.drop(columns=['Unnamed: 0'])


    if not all(feature in data.columns for feature in top_20_features):
        st.error("CSV must contain the correct top 20 gene features used to train the model.")
    else:
        input_df = data[top_20_features]  
        prediction = model.predict(input_df)
        st.success(f"Prediction: {prediction[0]}")
        st.write("Full Prediction Output:", prediction)