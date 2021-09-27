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

item_obj=APIRouter() #create a router object to manage endpoints
#get all items in databse
#response model is a configration which return pages of object passed 
@item_obj.get("/See all items", response_model=Page[Item_class], dependencies=[Depends(pagination_params)]) #return in the form of paginated tables
async  def read_data():
    #return all rows  from databse 
    return paginate((conn.execute(item_table.select()).fetchall())) #paginate tables

#search items using name of user 
@item_obj.get("/Search_with_name")
#takes name as input
async  def search(name:str): 
    #retune all items if user found
    return conn.execute(item_table.select().where (item_table.c.Name==name)).fetchall() 

#search items based on location
@item_obj.get("/Search_with_Location")
#takes location as input
async  def search(location:str):
    #return all items that match the location
    return conn.execute(item_table.select().where (item_table.c.Location==location)).fetchall()

#add new items in database
@item_obj.post("/Add Item")
#takes item object as input
#Depends has been used to take input in the form of form feilds 
#without depends we manually have to edit item object to add items in database
async  def write_data(item_Rob: Item_class=Depends()):
    #MYSQL Query to insert items in table
     conn.execute(item_table.insert().values(       
         Name=item_Rob.Name,
         Location=item_Rob.Location,
         Description=item_Rob.Description,
         Date=item_Rob.Date,
         others=item_Rob.others
    ))
    #show added item in response
     return item_Rob

#update items with respect to any feild
@item_obj.put("/Update Items")
#takes item object as input and if which is primary key to get specifically required item.
async  def update_data(id:int,item_Rob: Item_class=Depends()):
    conn.execute(item_table.update().values(
         Name=item_Rob.Name,
         Location=item_Rob.Location,
         Description=item_Rob.Description,
         Date=item_Rob.Date,
         others=item_Rob.others
    ).where (item_table.c.id==id))
    return item_Rob

#delete items based on input id
@item_obj.delete("/Delete Item")
async  def delete_data(id: int ):
    conn.execute(item_table.delete().where (item_table.c.id==id))
    
    return conn.execute(item_table.select()).fetchall()


