import streamlit as st
import numpy as np
import pandas as pd


add_selectbox = st.sidebar.radio(
    "Select the type of SEARCH METHOD",
    ("SIMILARITY SEARCH Method", "FAISS Method")
)

st.markdown('<style>body{background-color: #FFFFFF;}</style>',unsafe_allow_html=True)

if add_selectbox == 'SIMILARITY SEARCH Method' :
 st.title("Images using Similarity Search Method")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
    return pd.read_csv('method1.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 st.subheader("Choose an image from the dropdown : ")
 pic = st.selectbox('Choices : ', images)
 st.subheader("**_Image_** selected by the **_User_**:sunglasses:")
 st.image(pic,width=None)
 st.subheader('How Many Images do you want to see?')
 z = st.slider('How many images do you want to see?', 1, 10, 5)
 st.subheader("Similar Products you may want to buy")
 for index, row in df.iterrows():
     if row['0']==pic:
        while n < z+1:
            st.image(row[n], width = 100, caption=row[n])
            n+=1
            
elif add_selectbox == 'FAISS Method':
 st.title("Images using FAISS Method")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
    return pd.read_csv('faiss.csv')
 n=1
 df = get_data()
 images = df['0'].unique()
 st.subheader("Choose an image from the dropdown : ")
 pic = st.selectbox('Choices:', images)
 st.subheader("**_Image_** selected by the **_User_**:sunglasses:")
 st.image(pic,width=None)
 z = st.slider('How many images do you want to see?', 1, 10, 5)
 st.write("-------------------------------------------------------------------------------------------------")
 st.subheader("Similar Products you may want to buy")
 for index, row in df.iterrows():
     if row['0']==pic:
         while n < z+1:
            
             st.image(row[n], use_column_width=None, caption=row[n])
             n+=1



       
