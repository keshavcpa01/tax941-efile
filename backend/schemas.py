from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class Form941Create(BaseModel):
    ein: str
    quarter: str
    year: str
    wages: float
    withholding: float
    ss_wages: float
    medicare_wages: float