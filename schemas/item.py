from datetime import date
from pydantic import BaseModel
class Item_class(BaseModel):
   
    Name:str
    Location:str
    Description: str
    Date: date
    others:str
    
    