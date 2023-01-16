import streamlit as st
import pandas
import send_email

df = pandas.read_csv("topics.csv", sep=",")

topic_list = [line["topic"] for index, line in df.iterrows()]

with st.form(key="form") as form:
    st.text("Enter your email address: ")
    user_email = st.text_input("", key="email")

    st.text("Select the topic you would like to discuss: ")
    user_topic = st.selectbox("contact", topic_list,
                              key="topics")

    st.text("Enter your message: ")
    user_message = st.text_input("", key="user_message")

    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email.send_email(user_message, user_topic, user_email)
