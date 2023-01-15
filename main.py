import streamlit as st

st.set_page_config(layout="centered", page_title="About Me")

col1, col2 = st.columns(2)

with col1:
    st.write("<br><br>", unsafe_allow_html=True)
    image_filepath = "files/images/photo.png"
    st.image(image_filepath)

with col2:
    st.title("Who am I?")
    creator_info_text = """
    Hi there. My name is Kyle Galway. I am a student at Sheridan College's Software Development
    and Network Engineering program, currently completing my co-op semester. On the side, I am 
    also teaching myself numerous technologies, such as Python, Django, Flask, advanced Javascript,
    cloud computing, and more. I have a current grade point of average of 4.0 and am expecting to 
    graduate in December 2024.
    """
    st.info(creator_info_text)

st.write("Some projects I have completed include the following: ")
