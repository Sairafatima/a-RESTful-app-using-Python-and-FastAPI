from pydantic import BaseModel
from passlib.hash import bcrypt
class user_class(BaseModel):
   
    First_Name:str
    Last_Name:str
    password_hash: str
    username: str
