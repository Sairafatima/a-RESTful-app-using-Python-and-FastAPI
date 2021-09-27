
from datetime import date
from pydantic import BaseModel
#this class will be used to handle items from databse in form of objects
class Item_class(BaseModel):
   
    Name:str
    Location:str
    Description: str
    Date: date
    others:str
    

