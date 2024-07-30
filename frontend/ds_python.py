import streamlit as st
from pages import decorators, pydantic_use

def load_page():
    st.write("## Python for Data Science")

    # Projects Expander
    projects_expander = st.expander("Choose a Topic")

    with projects_expander:
        project_selection = st.radio("", ["Decorators", "Pydantic"])

    if project_selection == "Decorators":
        decorators.load_page()

    elif project_selection == "Pydantic":
        pydantic_use.load_page()
