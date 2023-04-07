import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import plotly.express as px
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "df.csv")
DATA_PATH1 = os.path.join(dir_of_interest, "data", "clean_df.csv")
pi=os.path.join(dir_of_interest, "data", "pipe.pkl")
df = pd.read_csv(DATA_PATH)
df1 = pd.read_csv(DATA_PATH1)
pipe = pickle.load(open(pi,"rb"))

st.dataframe(df1)
st.title("DATA VISULIAZATION")

st.write("please select the col inorder to compare with price")

col=st.selectbox('selsct one column',df.columns)
bar_df1=df[col].value_counts()
st.bar_chart(bar_df1)
fig_1 = px.box( df,x=col,y='MRP')
st.plotly_chart(fig_1,use_container_width=True)
st.write("AFTER CLEANING THE PRICE DATA BY DELETING THE OUTLIERS OF PRICE")
fig_1 = px.box( df1,x=col,y='MRP')
st.plotly_chart(fig_1,use_container_width=True)
