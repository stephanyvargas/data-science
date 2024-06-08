import streamlit as st
#from pages import mi_pj

def load_page():
    st.write("## Analysis for material informatics")
    st.write("""### Relevant Github links
    - [Awesome Materials Informatics](https://github.com/tilde-lab/awesome-materials-informatics)
    - [BestPractices](https://github.com/anthony-wang/BestPractices). Things that you should (and should not) do in your Materials Informatics research.
    - [A Highly Opinionated List of Open-Source Materials Informatics Resources](https://github.com/ncfrey/resources)
      """)
    
    # # Projects Expander
    # projects_expander = st.expander("Choose a Project")

    # with projects_expander:
    #     project_selection = st.radio("", ["Project 1"])

    # if project_selection == "Project_1":
    #     project.load_page()
