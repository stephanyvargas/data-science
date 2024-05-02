import streamlit as st
from pages import hugging_face, gaussian_processes, practical_statistics

def load_page():
    st.write("## Theory for Data Science")

    # Projects Expander
    projects_expander = st.expander("Choose a Topic")

    with projects_expander:
        project_selection = st.radio("", ["Practical Statistics",
                                          "Gaussian Processes"])

    if project_selection == "Practical Statistics":
        practical_statistics.load_page()

    elif project_selection == "Gaussian Processes":
        gaussian_processes.load_page()
