import streamlit as st

name = st.text_input("Please enter your name:")

if name:
    st.session_state.name = name

if st.button("Ok"):
    st.switch_page("pages/welcomPage.py")