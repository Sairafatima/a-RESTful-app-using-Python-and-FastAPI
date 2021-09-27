from fastapi import APIRouter
import jwt

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from tortoise import fields 
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model 
from config.db import conn
from models.index import item_table,user
from schemas.index import Item_class
from schemas.item import user_class
item_Rob=APIRouter()


user_obj=APIRouter()
@user_obj.post("/")
async def create_user(user_obj: user_class):
    conn.execute(user.insert().values(       
         First_Name=user_obj.First_Name,
         Last_Name=user_obj.Last_Name,
         username=user_obj.username,
         password_hash=bcrypt.hash(user_obj.password_hash)
    ))
  
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def authenticate_user(username: str, password: str):
    user = await user_class.get(username=username)
    if not user:
        return False 
    if not user.verify_password(password):
        return False
    return user 
 

@item_Rob.get("/")
async  def read_data():
   
    return conn.execute(item_table.select()).fetchall()

@item_Rob.get("/{id}")
async  def read_data(id:int):
    return conn.execute(item_table.select().where (item_table.c.id==id)).fetchall()
@item_Rob.post("/")
async  def write_data(item_Rob: Item_class):
     conn.execute(item_table.insert().values(
       
         Name=item_Rob.Name,
         Location=item_Rob.Location,
         Description=item_Rob.Description,
         Date=item_Rob.Date,
         others=item_Rob.others
    ))
     return conn.execute(item_table.select()).fetchall()

@item_Rob.put("/{id}")
async  def update_data(id: int ,item_Rob: Item_class):
    conn.execute(item_table.update().values(
        Name=item_Rob.Name,
         Location=item_Rob.Location,
         Description=item_Rob.Description,
         Date=item_Rob.Date,
         others=item_Rob.others
    ).where (item_table.c.id==id))
    return conn.execute(item_table.select()).fetchall()

@item_Rob.delete("/")
async  def delete_data(id: int ):
    conn.execute(item_table.delete().where (item_table.c.id==id))
    
    return conn.execute(item_table.select()).fetchall()


