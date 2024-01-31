import streamlit as st
import pandas as pd
import random

data = pd.read_csv('pos.csv', sep=',')

for index, info in data.iterrows():
    index += 1
    st.title(f"{index}. {info['name']}")
    st.image('images/' + info['image'])
    st.write(info['description'])
    st.subheader('Make It Hotter:')
    st.write(info['hotter'])
    st.write('------')