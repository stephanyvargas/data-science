# projects.py
import streamlit as st
from pages import hugging_face, gaussian_processes, practical_statistics

def load_page():
    st.write("## Projects")

    # Nested Projects Menu
    project_selection = st.sidebar.radio("Choose a Project:", ["Practical Statistics",
                                                               "Gaussian Processes"])

    if project_selection == "Practical Statistics":
        practical_statistics.load_page()

    elif project_selection == "Gaussian Processes":
        gaussian_processes.load_page()
