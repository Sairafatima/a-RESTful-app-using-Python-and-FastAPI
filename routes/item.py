from fastapi import APIRouter
from config.db import conn
from models.index import item_table
from schemas.index import Item_class
item_Rob=APIRouter()
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
async  def delete_data():
    conn.execute(item_table.delete().where (item_table.c.id==id))
    return conn.execute(item_table.select()).fetchall()