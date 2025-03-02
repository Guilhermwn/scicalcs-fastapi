from pydantic import BaseModel

class Uncertainties(BaseModel):
    measures: str
    uncertaintiesB: str