import streamlit as st

from utils.layout import add_separator_rainbow


def lottie_background(lottie_url):
    background_html = f"""
    <style>
        body {{
            margin: 0;
            padding: 0;
            overflow: hidden;
        }}
        #background {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }}
    </style>
    <div id="background">
        <lottie-player 
            autoplay 
            loop 
            background="transparent" 
            speed="1" 
            style="width: 100%; height: 100%;" 
            src="{lottie_url}">
        </lottie-player>
    </div>
    """
    return background_html


def render():
    st.title(":notebook: :gray[_WBS管理_] :notebook:")
    add_separator_rainbow()


