# projects.py
import streamlit as st
import hugging_face
import gaussian_processes
import practical_statistics

def load_page():
    st.write("## Projects")

    # Nested Projects Menu
    project_selection = st.sidebar.radio("Choose a Project:", ["Practical Statistics",
                                                               "Hugging Face", 
                                                               "Gaussian Processes"])

    if project_selection == "Practical Statistics":
        practical_statistics.load_page()
        
    elif project_selection == "Hugging Face":
        hugging_face.load_page()

    elif project_selection == "Gaussian Processes":
        gaussian_processes.load_page()

