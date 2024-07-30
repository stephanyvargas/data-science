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

    st.write("""When it comes to optional parameters, Pydantic handles then with no problem.
                So if you use `Union`, with `None` as an option, then Pydantic is ok if the parameter is there or not. If you use `Optional[]`, it expects the parameter to be sent, even if its blank. """)
    st.code("""
    from pydantic import BaseModel
    from typing import Union, Optional
    
    class MySecondModel(BaseModel):
        first_name: str
        middle_name: Union[str, None] # This means the parameter doesn't have to be sent
        title: Optional[str] # this means the parameter should be sent, but can be None
        last_name: str
    """)

    
if __name__ == "__main__":
    load_page()
    st.write("""We can use all the objects from the typing library and Pydantic will validate against them.
             """)
    st.code("""
            from pydantic import BaseModel
            from typing import Union, List, Dict
            from datetime import datetime
            
            class MyThirdModel(BaseModel):
                name: Dict[str, str]
                skills: List[str]
                holidays: List[Union[str, datetime]]
            
            # Example usage
            data = {
                "name": {"first": "John", "last": "Doe"},
                "skills": ["Python", "Data Science", "Machine Learning"],
                "holidays": ["2023-12-25", datetime(2024, 1, 1)]
            }
            
            # Creating an instance of MyThirdModel
            my_model_instance = MyThirdModel(**data)
            
            # Accessing attributes
            print(my_model_instance.name)        # Output: {'first': 'John', 'last': 'Doe'}
            print(my_model_instance.skills)      # Output: ['Python', 'Data Science', 'Machine Learning']
            print(my_model_instance.holidays)    # Output: [datetime.date(2023, 12, 25), datetime.datetime(2024, 1, 1, 0, 0)]
            
            # Modifying attributes
            my_model_instance.skills.append("AI")
            print(my_model_instance.skills)      # Output: ['Python', 'Data Science', 'Machine Learning', 'AI']
            
            # Validation and error handling
            try:
                invalid_data = {
                    "name": {"first": "Jane", "last": "Doe"},
                    "skills": ["Python", "Data Science", "Machine Learning"],
                    "holidays": ["Invalid Date String"]
                }
                invalid_model_instance = MyThirdModel(**invalid_data)
            except ValueError as e:
                print(e)
    """)

