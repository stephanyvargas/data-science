import streamlit as st
from frontend import projects, aboutme

st.set_page_config(page_title="Data Science Portfolio", layout="wide")

def main():
    tab1, tab2, tab3 = st.tabs(["Home", "Projects", "About Me"])

    if tab1:  # Home tab
        st.title("Welcome to My Data Science Portfolio")
        #st.image("data-visualization.jpg")  # Replace with your image
        #st.write("I'm a data science enthusiast with a passion for ...") 
        st.button("View Projects")
        st.button("Learn More About Me")

    elif tab2:
        projects.load_page()

    elif tab3:
        aboutme.load_page()

if __name__ == "__main__":
    main()
