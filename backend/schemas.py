from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class CompanyCreate(BaseModel):
    name: str
    ein: str
    address: str
    city: str
    state: str
    zip: str
    use_cpa_efin: bool = True
    client_efin: Optional[str] = None
    client_tcc: Optional[str] = None

class Form941Create(BaseModel):
    company_id: int
    quarter: str
    year: str
    wages: float
    withholding: float
    ss_wages: float
    medicare_wages: float
