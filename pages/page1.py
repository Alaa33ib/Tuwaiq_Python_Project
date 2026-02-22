import streamlit as st

st.title("Page 1")

st.write("This is Page 1")

if st.button("Back to Home"):
    st.switch_page("pages/welcomPage.py")
