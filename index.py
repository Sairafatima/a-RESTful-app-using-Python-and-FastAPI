from fastapi import FastAPI
from routes.index import item_obj,user_obj,csv_obj
from fastapi import FastAPI, Depends, HTTPException, status
app=FastAPI()
app.include_router(item_obj)
app.include_router(user_obj)
app.include_router(csv_obj)