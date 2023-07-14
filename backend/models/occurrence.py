from pydantic import BaseModel

class Occurrence(BaseModel):
    occID: str
    victim_name: str
    victim_surname: str
    victim_ID: str # Their id number 
    cellphone: str
    telephone: str
    email: str
    residential_address: str
    occurance_description: str 
    observations_other_info: str
    attending_officer_id: str

