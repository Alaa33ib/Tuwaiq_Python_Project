import streamlit as st

class Background:
    def __init__(self, image_url):
        self.image_url = image_url

    def set_page_bg(self):
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("{self.image_url}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
