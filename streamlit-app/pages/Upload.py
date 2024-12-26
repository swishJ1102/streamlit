import streamlit as st

def render():
    st.title("文件上传")
    uploaded_file = st.file_uploader("选择一个文件")
    if uploaded_file:
        st.success(f"文件 `{uploaded_file.name}` 上传成功！")