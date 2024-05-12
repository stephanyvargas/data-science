import streamlit as st
from pages import hugging_face, paper_prometheus, language_agent_tree_search

def load_page():
    st.write("## LLMs for Data Science")

    # Projects Expander
    projects_expander = st.expander("Choose a Topic")

    with projects_expander:
        project_selection = st.radio("", ["Hugging Face", "Evaluate LLMs: Prometheus2"])

    if project_selection == "Hugging Face":
        hugging_face.load_page()

    elif project_selection == "Evaluate LLMs: Prometheus2":
        paper_prometheus.load_page()

    elif project_selection == "Llama: Language Agent Tree Search":
        language_agent_tree_search.load_page()
