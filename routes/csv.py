from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_pagination import Page, add_pagination, paginate, pagination_params
from passlib.hash import bcrypt
from fastapi import FastAPI, Form,UploadFile,File
import jwt
import pandas as pd
from config.db import conn
from models.index import item_table
from datetime import datetime
import locale
import shutil   
import time
csv_obj=APIRouter()


@csv_obj.post("/upload files")
async  def read_data(file_obj: UploadFile = File(...)):
    #return all rows  
    with open("des.csv", "wb") as buffer:
        shutil.copyfileobj(file_obj.file, buffer)
  
    data = pd.read_csv("des.csv" ,compression='infer',date_parser=True)
    data_list = data.values
    for line in  data_list:
        print(line)          
        date_time_obj = datetime.strptime(line[3], '%m/%d/%Y %H:%M')
        conn.execute(item_table.insert().values(       
        Name=line[0],
        Location=line[1],
        Description=line[2],
        Date=date_time_obj,
        others=line[4]
    ))