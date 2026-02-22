import streamlit as st

class Background:
    def __init__(self, image_url):
        self.image_url = image_url

    def set_page_bg(self):
        st.markdown(
            f"""
            <style>
            /* 1. THE BACKGROUND (Blurred) */
            [data-testid="stAppViewContainer"] {{
                background-image: url("{self.image_url}");
                background-size: cover;
                background-attachment: fixed;
            }}
            
            [data-testid="stAppViewContainer"]::before {{
                content: "";
                position: fixed;
                top: 0; left: 0; right: 0; bottom: 0;
                background: inherit;
                filter: blur(6px);
                -webkit-filter: blur(6px);
                z-index: -1;
                transform: scale(1.1);
            }}

            /* 2. PROGRESS BAR FIX: Removing the glass bubble */
            /* This targets the container of the progress bar specifically */
            div[data-testid="stProgress"] > div {{
                background-color: rgba(255, 255, 255, 0.2) !important;
            }}
            
            /* This kills the glass box around the progress area */
            [data-testid="stVerticalBlock"] > div:has(div[data-testid="stProgress"]) {{
                background: transparent !important;
                backdrop-filter: none !important;
                border: none !important;
                box-shadow: none !important;
            }}

            /* 3. MENU & FONT FIX: Back to basics to save the icons */
            html, body, p, div {{
                font-family: sans-serif !important;
            }}

            /* 4. LIGHT GLASS BOXES (Tint Removed) */
            [data-testid="stVerticalBlock"] > div:has(div.stRadio), 
            .stMarkdown, .stButton {{
                background: rgba(255, 255, 255, 0.1) !important; /* Back to 10% white */
                backdrop-filter: blur(10px);
                border-radius: 15px;
                padding: 20px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
                margin-bottom: 10px;
            }}

            /* 5. TEXT SHADOWS (Kept for readability on light glass) */
            h1, h2, h3, p, li {{
                color: white !important;
                text-shadow: 2px 2px 8px rgba(0, 0, 0, 1) !important; 
            }}
            </style>
            """,
            unsafe_allow_html=True
        )