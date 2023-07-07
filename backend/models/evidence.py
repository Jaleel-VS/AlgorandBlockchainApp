from pydantic import BaseModel

class Evidence(BaseModel):
    evidence_description: str
    evidence_origin: str
    evidence_content: bytes