
import streamlit as st
import styles.background as background

st.set_page_config(page_title="Welcome", layout="centered")

#bakground
bg = background.Background("https://preview.redd.it/bnef3fhuqm261.png?width=1080&crop=smart&auto=webp&s=c99ad19012ed7569db81a9b40732bea7828f0aae")
bg.set_page_bg()

def discription():
    st.header("Quiz discription:")
    st.write("This quiz is designed to check what personality you are, you may choose the theme of the quiz, and answer the questions, at the end you will get your personality type and a description about it.")
    st.write("Please choose an option below:")

if "name" not in st.session_state:
    st.session_state.name = None

if st.session_state.name is None:
# Change #FFD700 to any color code you like!
    st.markdown("<span style='color: white; font-size: 32px; font-weight: bold; text-shadow: 2px 2px 5px black;'>Hello There !!</span>", unsafe_allow_html=True)    
    st.markdown("<p style='color: white; font-size: 18px; font-weight: bold; text-shadow: 1px 1px 3px black; margin-bottom: -35px;'>Please enter your name:</p>", unsafe_allow_html=True)
    name = st.text_input("", placeholder="Your Name.", key="user_name_input")
    if st.button("Ok"):
        if name:
            st.session_state.name = name
            st.rerun() # Refresh to show the menu below
else:
    st.write(f"Hello, {st.session_state.name} !!")
    discription()
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        c1, c2 = st.columns(2)

        with c1:
            if st.button("Detective Conan Quiz"):
                st.switch_page("pages/Quiz1.py")

        with c2:
            if st.button("SpongeBob SquarePants Quiz"):
                st.switch_page("pages/Quiz2.py")
