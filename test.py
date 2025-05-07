import streamlit as st

col1, col2 = st.columns([2, 3])
tab1, tab2 = st.tabs(['tab a', 'tab b'])
with col1 :
    st.title("here is colun1 title")
    with tab1:
        st.write("hello")
    with tab2:
        st.write("world")

with col2 :
    st.title("here is colun2 title")
    st.checkbox("this is cheak box")
col1.subheader("i am lotte giants")
col2.subheader("wijfknf")