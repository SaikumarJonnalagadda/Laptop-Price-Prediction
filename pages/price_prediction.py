import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "df.csv")
pi=os.path.join(dir_of_interest, "data", "pipe.pkl")
df = pd.read_csv(DATA_PATH)
pipe = pickle.load(open(pi,"rb"))

st.title("Laptop Price Predictor")

Brand = st.selectbox("Select the Brand:- ", df["Brand"].unique())
processor = st.selectbox("Select the Processor:- ", df["processor"].unique())
Ram_type= st.selectbox("Select the RAM TYPE:- ", df["RAM TYPE"].unique())
Ram_size= st.selectbox("Select the RAM SIZE:- ", df["RAM"].unique())
os = st.selectbox("Select the Operating Syatem:- ", df["os"].unique())
ROM_TYPE= st.selectbox("Select the ROM TYPE:- ", df["ROM_TYPE"].unique())
ROM_SIZE= st.selectbox("Select the ROM Storage:- ", df["ROM_SIZE"].unique())
button = st.button("Predict ❗")
if button:
    query = np.array([processor,Ram_size,os,Ram_type,Brand,ROM_SIZE,ROM_TYPE])
    query = query.reshape(1, -1)
    prediction = str(int(np.exp(pipe.predict(query)[0])))
    st.title("The predicted price of this configuration is " + prediction)