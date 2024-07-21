import streamlit as st

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photoo.jpg", width=220)

with col2:
    st.title("Rayyan Shabbir")
    content = """
    I am a Software engineers, and interest in AI.
    I have done my bachelors in IT from PUCIT, and below are all my projects.
"""
    st.info(content)
