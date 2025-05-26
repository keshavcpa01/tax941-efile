from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class Form941(Base):
    __tablename__ = "form941s"
    id = Column(Integer, primary_key=True, index=True)
    ein = Column(String, index=True)
    quarter = Column(String)
    year = Column(String)
    wages = Column(Float)
    withholding = Column(Float)
    ss_wages = Column(Float)
    medicare_wages = Column(Float)