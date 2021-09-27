
from datetime import date
from pydantic import BaseModel
from tortoise.models import Model 
from passlib.hash import bcrypt
class Item_class(BaseModel):
   
    Name:str
    Location:str
    Description: str
    Date: date
    others:str
    
class user_class(BaseModel):
   
    First_Name:str
    Last_Name:str
    password_hash: str
    username: str
    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)
