import streamlit as st
import pandas

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1:
    st.image("images/photoo.jpg")

with col2:
    st.title("Rayyan Shabbir")
    content = """
    I am a Software engineers, and interest in AI.
    I have done my bachelors in IT from PUCIT.
    I am skilled in Python, Java, C, Cpp, ML and DL. 
    I wanted to serve people and channge their lives with technology.

    IT is future, and everyone must put efforts to come on that side where you will control technology.
    
    If you are from some other degree like business, marketinng, construction or any other, you can also switch to IT.
    As, there are many resources available online, and the most popular sites are coursera, udemy, edureka, educative etc.

    Explore these and take the first step.
    """
    st.info(content)

content2 = "Below you can find some of apps I have built in Python. Feel free to contact me!"
st.write(content2)


col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])