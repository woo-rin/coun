import streamlit as st

col1, col2 = st.columns([2, 3])
with col1 :
    st.title("here is colun1 title")

with col2 :
    st.title("here is colun2 title")
    st.checkbox("this is cheak box")