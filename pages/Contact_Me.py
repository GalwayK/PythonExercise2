import streamlit
import send_email

streamlit.set_page_config(page_title="Contact Me")
streamlit.header("Contact Me")

with streamlit.form(key="email_form"):
    streamlit.text("Your email address: ")
    user_email = streamlit.text_input("", key="user_email")

    streamlit.text("Your subject: ")
    user_subject = streamlit.text_input("", key="user_subject")

    streamlit.text("Your message: ")
    user_message = streamlit.text_area("", key="user_message")

    submit_button = streamlit.form_submit_button("Submit")

    if submit_button:
        print(f"Email: {user_email}\nMessage: {user_message}")
        send_email.send_email(user_message, user_subject, user_email)
