from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
import jwt
#database connection import
from config.db import conn
#tables import
from models.index import item_table
#class models import
from schemas.index import Item_class
item_obj=APIRouter()

@item_obj.get("/See all items")
async  def read_data():
    #return all rows   
    return conn.execute(item_table.select()).fetchall()

@item_obj.get("/Search")
async  def search(item_Rob: Item_class):
    return conn.execute(item_table.select().where (item_table.c.id==item_Rob.id) | item_table.select().where (item_table.c.Name==item_Rob.Name)).fetchall()


@item_obj.post("/Add Item")
async  def write_data(item_Rob: Item_class):
     conn.execute(item_table.insert().values(       
         Name=item_Rob.Name,
         Location=item_Rob.Location,
         Description=item_Rob.Description,
         Date=item_Rob.Date,
         others=item_Rob.others
    ))
     return conn.execute(item_table.select()).fetchall()


@item_obj.put("/Update Items")
async  def update_data(item_Rob: Item_class):
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


