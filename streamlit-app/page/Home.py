import streamlit as st
import random
from utils.layout import add_separator_rainbow


def render():
    print("top_page", st.session_state['name'])
    st.title(":cherry_blossom: :gray[_トップページ_] :cherry_blossom:")
    add_separator_rainbow()

    st.markdown(f'*{st.session_state["name"][:1]}さん、お疲れさまでした。*')
    st.markdown('_今日も頑張りましょう。_')
    st.balloons()
