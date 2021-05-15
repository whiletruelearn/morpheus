import streamlit as st

def log(msg,use_streamlit=True):
    if use_streamlit:
        st.write(msg)
    print(msg)