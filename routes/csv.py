#this route accepts CVS File in specific formate to update items data
from fastapi import FastAPI, Depends,APIRouter
from fastapi import FastAPI, Form,UploadFile,File
import jwt
import pandas as pd
from config.db import conn
from models.index import item_table
from datetime import datetime
import locale
import shutil   

csv_obj=APIRouter()

#takes file object as input
@csv_obj.post("/upload files")
async  def read_data(file_obj: UploadFile = File(...)):
    #copy file to a temporary file on server
    with open("temp.csv", "wb") as buffer:
        shutil.copyfileobj(file_obj.file, buffer) 
    #read temporary file and uodate database

    data = pd.read_csv("temp.csv" ,compression='infer',date_parser=True) 
    #convert pandas dataframes to list
    data_list = data.values
    for line in  data_list:     
        #for all rows it is important to change date strings into actual date object for insertion in database   
        date_time_obj = datetime.strptime(line[3], '%m/%d/%Y %H:%M')
        conn.execute(item_table.insert().values(       
        Name=line[0],
        Location=line[1],
        Description=line[2],
        Date=date_time_obj,
        others=line[4]
    ))
    return ("Rords uploaded")