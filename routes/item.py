from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_pagination import Page, add_pagination, paginate, pagination_params
from passlib.hash import bcrypt
from fastapi import FastAPI, Form
import jwt
#database connection import
from config.db import conn
#tables import
from models.index import item_table
#class models import
from schemas.index import Item_class


item_obj=APIRouter()
#get all items in databse
@item_obj.get("/See all items", response_model=Page[Item_class], dependencies=[Depends(pagination_params)]) #return in the form of paginated tables
async  def read_data():
    #return all rows   
    return paginate((conn.execute(item_table.select()).fetchall()))

@item_obj.get("/Search_with_name")
async  def search(name:str):
    return conn.execute(item_table.select().where (item_table.c.Name==name)).fetchall()
@item_obj.get("/Search_with_Location")
async  def search(location:str):
    return conn.execute(item_table.select().where (item_table.c.Location==location)).fetchall()


@item_obj.post("/Add Item")
async  def write_data(item_Rob: Item_class=Depends()):
     conn.execute(item_table.insert().values(       
         Name=item_Rob.Name,
         Location=item_Rob.Location,
         Description=item_Rob.Description,
         Date=item_Rob.Date,
         others=item_Rob.others
    ))
     return conn.execute(item_table.select()).fetchall()


@item_obj.put("/Update Items")

async  def update_data(id:int,item_Rob: Item_class=Depends()):
    conn.execute(item_table.update().values(
         Name=item_Rob.Name,
         Location=item_Rob.Location,
         Description=item_Rob.Description,
         Date=item_Rob.Date,
         others=item_Rob.others
    ).where (item_table.c.id==id))
    return conn.execute(item_table.select()).fetchall()

@item_obj.delete("/Delete Item")
async  def delete_data(id: int ):
    conn.execute(item_table.delete().where (item_table.c.id==id))
    
    return conn.execute(item_table.select()).fetchall()


