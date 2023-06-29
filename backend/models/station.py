from pydantic import BaseModel

class Station(BaseModel):
    unitNumber: str
    address: str
    province: str
