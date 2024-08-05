# pydantic_use.py
import streamlit as st
from functools import wraps
import time

def load_page():
    # **1. Introduction**
    st.header("What is Pydantic?")
    st.write("https://medium.com/@marcnealer/a-practical-guide-to-using-pydantic-8aafa7feebf6")
    st.write("Pydantic v1 is Python Dataclasses with validation, serialization and data transformation functions. So you can use Pydantic to check your data is valid. transform data into the shapes you need, and then serialize the results so they can be moved on to other applications.")
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

    st.write("""## Applying Default Values""")
    st.write("""    
                In a standard Python class, if you define a mutable default argument in the `__init__` method, it leads to the issue of shared mutable defaults.
                This is a problem and that is with the definition of the list. 
                If you code a model in this way, only one list object is created and its shared between all instances of this model. 
                The same happens with dictionaries etc.
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

    st.write("""## Field Validation""")
    st.write("""The example is validating the data before the default validation. 
    This is really useful as it gives us a chance to change and reformat the data, as well as validating. 
    In this case I’m expecting a numerical time stamp to be passed. I validate for that and then convert the timestamp to a datetime object. 
    The default validation is expecting a datetime object. The `@validator` decorator in Pydantic is used to define custom validation logic for model fields. 
    The `pre=True` argument indicates that the validation function should be run before any other validation logic. 
    This is particularly useful when you need to preprocess or transform the input data before the standard validation rules are applied.""")
    
    st.code("""
                from pydantic import BaseModel, validator, ValidationError
                import datetime
                from typing import Any
                
                
                def stamp2date(value: Any) -> datetime.datetime:
                    if not isinstance(value, (float, int)):  # Allow both float and int for timestamp
                        raise ValueError("incoming date must be a timestamp")
                    try:
                        res = datetime.datetime.fromtimestamp(value)
                    except ValueError:
                        raise ValueError("Time stamp appears to be invalid")
                    return res
                
                
                class DateModel(BaseModel):
                    dob: datetime.datetime

                    ## Custom validator for the 'dob' field
                    @validator('dob', pre=True)
                    def validate_dob(cls, value):
                        return stamp2date(value)
                
                # Testing with valid and invalid inputs
                try:
                    valid_date_model = DateModel(dob=1627849183.0)  # Valid timestamp
                    print('good', valid_date_model) # good dob=datetime.datetime(2021, 8, 2, 5, 19, 43)
                except ValidationError as e:
                    print(e)
                
                try:
                    invalid_date_model = DateModel(dob="not a timestamp")  # Invalid timestamp
                except ValidationError as e:
                    print(e) #  incoming date must be a timestamp (type=value_error)
        """)
    st.write("""Multiple validaros can also be achieved.""")

    st.code("""
                from pydantic import BaseModel, validator, ValidationError
                import datetime
                from typing import Any
                
                
                def stamp2date(value: Any) -> datetime.datetime:
                    if not isinstance(value, (float, int)):  # Allow both float and int for timestamp
                        raise ValueError("incoming date must be a timestamp")
                    try:
                        res = datetime.datetime.fromtimestamp(value)
                    except ValueError:
                        raise ValueError("Time stamp appears to be invalid")
                    return res
                
                def one_year(value: datetime.datetime) -> datetime.datetime:
                    if value < datetime.datetime.today() - datetime.timedelta(days=365):
                        raise ValueError("the date must be less than a year old")
                    return value
                
                class DateModel(BaseModel):
                    dob: datetime.datetime
                
                    @validator('dob', pre=True)
                    def validate_dob_pre(cls, value):
                        return stamp2date(value)
                    
                    @validator('dob')
                    def validate_dob_post(cls, value):
                        return one_year(value)
                
                
                # Testing with valid and invalid inputs
                try:
                    valid_date_model = DateModel(dob=1727849183.0)  # Valid timestamp
                    print(valid_date_model) # dob=datetime.datetime(2024, 10, 2, 15, 6, 23)
                except ValidationError as e:
                    print(e)
                
                try:
                    invalid_date_model = DateModel(dob=1262304000.0)  # Timestamp older than a year
                except ValidationError as e:
                    print(e) # the date must be less than a year old (type=value_error)
                """)


if __name__ == "__main__":
    load_page()
