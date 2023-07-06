# Officers will have to log into this system 
# The models folder is for the user models
# We deifine our table structure here
# This is the  model that we save inside our mongodb. This is our collection

from pydantic import BaseModel # Pydantic is a Python library data parsing and validation. It uses the type hinting mechanism of the newer versions of Python and validates the types during runtime. 
# Pydantic defines BaseModel class.  It acts as the base class for creating user defined models


class UserLogin(BaseModel):
    username: str
    password: str
    



    




