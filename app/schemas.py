from pydantic import BaseModel



class UserLogin(BaseModel):
    email: str
    password: str

class User(UserLogin):
    id: int
    name: str
    role:str

class Projet(BaseModel):
    id :int 
    url :str 
    date :str 
    total_vulnerability :str 
    high :bool 
    medium :bool 
    low :bool  

class Dynamicscan(BaseModel):
    id :int 
    url :str 
    date :str 
    total :str 
    high :bool 
    medium :bool 
    low :bool      
    status :str
    scanner :str

class Infrastructure(BaseModel):
    id :int 
    target :str 
    date :str 
    total :str 
    high :bool 
    medium :bool 
    low :bool      
    status :str
    scanner :str

class Connectors(BaseModel):
    id :int
    name :str
    status :str
    date :str
    




