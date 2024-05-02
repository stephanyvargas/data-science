import streamlit as st
import ds_theory, ds_python, ds_analysis, ds_llms
import app_chat, app_pomodoro
import aboutme

st.set_page_config(page_title="Data Science Portfolio", layout="wide")

def main():

    #st.title("Welcome to Data Science!")

    with st.sidebar:
        #home_button = st.button("Home")

        # Projects Expander
        option = st.selectbox("Data Science",
                                ("Explore Theory",
                                "Explore Python",
                                "Analysis",
                                "LLMs") )

        # Chat Expander
        chat_expander = st.expander("Apps")
        with chat_expander:
            chat_button = st.button("Let's Chat")
            pomodoro_button = st.button("Pomodoro Clock")

    if option == "Explore Theory":
        st.title("Explore Theory!")
        ds_theory.load_page()

    elif option == "Explore Python":
        st.title("Explore Python!")
        ds_python.load_page()

    elif option == "Analysis":
        st.title("Analysis!")
        ds_analysis.load_page()

    elif option == "LLMs":
        st.title("Explore LLMs!")
        ds_llms.load_page()

    elif chat_button:
        st.title("Let's Chat!")
        app_chat.load_page()

    elif pomodoro_button:
        st.title("Let's Study!")
        app_pomodoro.load_page()

if __name__ == "__main__":
    main()
