import streamlit as st
import base64
# from os import write
import os

class Background:
    def __init__(self, png_file):
        self.png_file = png_file

    def set_png_as_page_bg(self):
        with open(self.png_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        ext = os.path.splitext(self.png_file)[1].lower()
        mime = "png" if ext == ".png" else "jpeg"
        st.markdown(
            f"""
            <style>
            [data-testid="stAppViewContainer"] > .main {{
                background-image: url("data:image/{mime};base64,{bin_str}");
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# set_png_as_page_bg('bnef3fhuqm261.webp')
