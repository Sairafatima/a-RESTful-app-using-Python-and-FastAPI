from fastapi import FastAPI
from routes.index import items
app=FastAPI()
app.include_router(items)
