import streamlit as st
from pages import project

def load_page():
    st.write("## Analysis projects for Data Science")

    # Projects Expander
    projects_expander = st.expander("Choose a Project")

    with projects_expander:
        project_selection = st.radio("", ["Project 1"])

    if project_selection == "Project_1":
        project.load_page()
