
from pydantic import BaseModel

class Docket(BaseModel):
    name: str
    email: str
    phone: str