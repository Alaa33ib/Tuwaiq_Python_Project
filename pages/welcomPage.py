from os import write

import streamlit as st
import Background.background as background

st.set_page_config(page_title="Welcome", layout="centered")

def discription():
    st.header("Quiz discription:")
    st.write("This quiz is designed to check what personality you are, you may choose the theme of the quiz, and answer the questions, at the end you will get your personality type and a description about it.")
    st.write("Please choose an option below:")

if "name" in st.session_state:
    st.write(f"Hello, {st.session_state.name} 👋")
    discription()

else:
    st.write("Hello There👋")
    discription()

col1, col2, col3 = st.columns([1,2,1])

with col2:
    c1, c2 = st.columns(2)

    with c1:
        if st.button("Detective Conan Quiz"):
            st.switch_page("pages/quiz.py")

    with c2:
        if st.button("Page 2"):
            st.switch_page("pages/page2.py")