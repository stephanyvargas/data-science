# app.py
import streamlit as st
from frontend import projects, aboutme

# Page Config
st.set_page_config(page_title="Data Science Portfolio", layout="wide")

def main():
    st.title("Welcome to My Data Science Portfolio")

    # Main Menu Selection
    menu = st.sidebar.radio("", ["Home", "Projects", "About Me"])

    if menu == "Home":
        st.write("This is a basic portfolio showcasing my data science projects and skills.")
        
    elif menu == "Projects":
        projects.load_page()

    elif menu == "About Me":
        aboutme.load_page()

if __name__ == "__main__":
    main()

