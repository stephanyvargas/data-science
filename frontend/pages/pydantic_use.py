# pydantic_use.py
import streamlit as st
from functools import wraps
import time

def load_page():
    # **1. Introduction**
    st.header("## What is Pydantic?")
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
                "holidays": ["2023-01-01", datetime(2024, 1, 1)]
            }
            
            # Creating an instance of MyThirdModel
            my_model_instance = MyThirdModel(**data)
            
            # Accessing attributes
            print(my_model_instance.name)        # Output: {'first': 'John', 'last': 'Doe'}
            print(my_model_instance.skills)      # Output: ['Python', 'Data Science', 'Machine Learning']
            print(my_model_instance.holidays)    # Output: [datetime.date(2024, 1, 1), datetime.datetime(2024, 1, 1, 0, 0)]
            
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

    st.write("""## Applying Default Values
                In a standard Python class, if you define a mutable default argument in the __init__ method, it leads to the issue of shared mutable defaults.
                This is a problem and that is with the definition of the list. 
                If you code a model in this way, only one list object is created and its shared between all instances of this model. The same happens with dictionaries etc.
             """)
    st.code("""
            class ProblematicModel:
                def __init__(self, names=[]):
                    self.names = names
            
            # Creating instances of ProblematicModel
            instance_1 = ProblematicModel()
            instance_2 = ProblematicModel()
            
            # Modifying the list in one instance
            instance_1.names.append("John")
            
            # Printing the lists in both instances
            print(instance_1.names)  # Output: ['John']
            print(instance_2.names)  # Output: ['John']
            """)
    
    st.write(""" To correct this in a standard Python class, you would use None as the default value and initialize the list inside the `__init__` method.""")
    st.code("""
            class CorrectedModel:
                def __init__(self, names=None):
                    if names is None:
                        names = []
                    self.names = names
            
            # Creating instances of CorrectedModel
            instance_1 = CorrectedModel()
            instance_2 = CorrectedModel()
            
            # Modifying the list in one instance
            instance_1.names.append("John")
            
            # Printing the lists in both instances
            print(instance_1.names)  # Output: ['John']
            print(instance_2.names)  # Output: []
            """)
    
    st.write("""If you directly assign a mutable default value to a Pydantic model field, it might not show the issue immediately due to how Pydantic handles initialization, but the underlying problem is the same.
                To correct this in Pydantic, use `Field(default_factory=...)`.
            """)
    st.code("""
                from pydantic import BaseModel
                
                class ProbrematicPydanticModel(BaseModel):
                    first_name: str = "jane"
                    middle_names: list = []
                    last_name : str = "doe"
            """)

    st.write("""Notice that a class or function is passed to the default factory and not a instance of such. This results in a new instance being created for all instances of the model.
                If you have been looking at the Pydantic documentation, you would see the Field class being used in lots of different ways. 
                However, the more I use Pydantic, the less I used the Field Object. It can do a lot of things, but it can also make life complicated. 
                For the defaults and default factory, its the way to go. """)
    st.code("""
                from pydantic import BaseModel, Field
                
                class DefaultsModel(BaseModel):
                    first_name: str = "jane"
                    middle_names: list = Field(default_factory=list)
                    last_name: str = "doe"
        """)

if __name__ == "__main__":
    load_page()
