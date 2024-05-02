import streamlit as st
from pages import hugging_face

def load_page():
    st.write("## LLMs for Data Science")

    # Projects Expander
    projects_expander = st.expander("Choose a Topic")

    with projects_expander:
        project_selection = st.radio("", ["Hugging Face"])

    if project_selection == "Hugging Face":
        practical_statistics.load_page()
