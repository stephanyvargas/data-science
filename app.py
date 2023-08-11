import streamlit as st

# Page Config
st.set_page_config(page_title="Data Science Portfolio", layout="wide")

def main():
    st.title("Welcome to My Data Science Portfolio")

    menu = ["Home", "Projects", "About Me"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("This is a basic portfolio showcasing my data science projects and skills.")
        
    elif choice == "Projects":
        st.write("Coming Soon: Here, I will showcase my data science projects, analyses, and models.")

    elif choice == "About Me":
        st.write("""
        ## About Me
        I am a budding data scientist with a passion for unlocking insights from data.
        """)
        st.image("assets/profile_picture.jpg", use_column_width=True)

if __name__ == "__main__":
    main()

