
from pydantic import BaseModel

class Docket(BaseModel):
    name: str
    email: str
    phone: str
    # caseID: str # Automatically generated 
    # Id:str
    # names: str
    # surnames: str
    # email: str
    # phone: str
    # cellphone: str
    # homephone: str
    # residential_address: str
    # Victim_statement:bytes
