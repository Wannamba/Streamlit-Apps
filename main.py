import streamlit as st

header = st.container()
dataset = st.container()
features = st.container()
model_training =  st.container()

with header:
    st.title('Welcome to the first app')
    st.text('in this project, ....0')

with dataset:
    st.header('Dataset')

with features:
    st.header('features')

with model_training:
    st.header('train the model')


