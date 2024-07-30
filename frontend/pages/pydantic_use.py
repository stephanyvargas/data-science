# pydantic_use.py
import streamlit as st
from functools import wraps
import time

def load_page():
    # **1. Introduction**
    st.header("What is Pydantic?")
    st.write("Pydantic is Python Dataclasses with validation, serialization and data transformation functions. So you can use Pydantic to check your data is valid. transform data into the shapes you need, and then serialize the results so they can be moved on to other applications.")
    st.write("**A REALLY Basic example**")
    st.code("""
    from pydantic import BaseModel

    class MyFirstModel(BaseModel):
        first_name: str
        last_name: str
    
    validating = MyFirstModel(first_name="marc", last_name="nealer")
    """)
