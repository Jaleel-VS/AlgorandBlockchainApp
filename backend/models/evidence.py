from pydantic import BaseModel

class Evidence(BaseModel):
    case_Id:str
    evidence_description: str
    evidence_origin: str
    associated_officer: str
    evidence_content: bytes