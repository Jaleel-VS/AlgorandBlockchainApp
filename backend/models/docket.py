
from pydantic import BaseModel


class Docket(BaseModel):
    # Generated automatically
    occ_ID: str # This needs to be passed from mongodb
    docket_ID:str 
    relevant_officer: str

    # Offense details 
    offense_category: str 
    day_of_offense: str 
    time_of_offense: str
    offense_type: str
    offense_description: str
    crime_code: str
    property_damage_or_injuries: str

    # Accused details 
    accused_name: str
    accused_surname: str
    accused_race: str
    accused_gender: str
    accused_age:str
    accused_description: str
    accused_last_seen: str
    
    
    
    
   
