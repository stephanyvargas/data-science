import streamlit as st

def load_page():
    # **1. Introduction**
    st.header("What are decorators?")
    st.subheader("Examples")
    st.write("... Explanation with the gift-wrapping analogy ...")
    st.write("**Why use them?** ... Benefits ...")
    st.write("**Syntax Example**")
    
    st.code("""
    def logging_decorator(func): 
        # ...
        
    def timer_decorator(func):
        # ... (Code from above)
    """) 
    
if __name__ == "__main__":
    load_page()
