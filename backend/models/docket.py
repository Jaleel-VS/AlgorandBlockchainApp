
from pydantic import BaseModel

class Docket(BaseModel):
    name: str
    email: str
    phone: str

    # Id:str
    # names: str 
    # surnames: str
    # cellphone: str
    # homephone: str
    # residential_address: str
    # Victim_statement:bytes
