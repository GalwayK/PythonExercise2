import streamlit
import pandas

streamlit.set_page_config(page_title="Company Website")

streamlit.title("The Best Company")
company_text = """
Here at The Best Company, we proudly maintain our standards for performance, employee
satisfaction, and customer appreciation. We've ranked first five years in a row for 
best North American company, and have five gold medals in being a really good company.
"""
streamlit.info(company_text)
streamlit.subheader("Our Team")

df = pandas.read_csv("data.csv")
len_df = len(df)
col_one_index = int(len_df / 3)
col_two_index = int((len_df / 3) * 2)
col1, space_one, col2, space_two, col3 = streamlit.columns([5, 1, 5, 1, 5])

with col1:
    for index, row in df[:col_one_index].iterrows():
        first_name = row['first name'].title()
        last_name = row['last name'].title()
        streamlit.subheader(f"{first_name} {last_name}")
        role = row["role"]
        streamlit.write(role)
        image_path = row['image']
        streamlit.image(f"images/{image_path}")

with col2:
    for index, row in df[col_one_index:col_two_index].iterrows():
        first_name = row['first name'].title()
        last_name = row['last name'].title()
        streamlit.subheader(f"{first_name} {last_name}")
        role = row["role"]
        streamlit.write(role)
        image_path = row['image']
        streamlit.image(f"images/{image_path}")

with col3:
    for index, row in df[col_two_index:].iterrows():
        first_name = row['first name'].title()
        last_name = row['last name'].title()
        streamlit.subheader(f"{first_name} {last_name}")
        role = row["role"]
        streamlit.write(role)
        image_path = row['image']
        streamlit.image(f"images/{image_path}")

streamlit.subheader("This web application was created by Kyle Galway")
