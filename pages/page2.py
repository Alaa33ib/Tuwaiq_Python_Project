import streamlit as st

st.title("Page 2")

st.write("This is Page 2")

if st.button("Back to Home"):
    st.switch_page("pages/welcomPage.py")
