import streamlit as st
from matplotlib import image
import os
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "laptop.jfif")

st.title("JONNALAGADDA SAIKUMAR")
st.header("lets CONNECT:")
st.write("LINKDIN: [link](https://www.linkedin.com/in/saikumar-jonnalagadda-305003215)")
st.write("GITHUB: [link](https://github.com/SaikumarJonnalagadda)")
    
    

btn_click1 = st.button("Click Me!")

if btn_click1 == True:
    st.header("PRICE PRDICTION OF LAPTOP")
    st.balloons()
