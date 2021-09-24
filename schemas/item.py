from datetime import date
from pydantic import BaseModel
class Item_class(BaseModel):
    id: int
    Name:str
    Location:str
    Description: str
    Date: date
    others:str
    
    