from fastapi import FastAPI
from routes.index import item_Rob
app=FastAPI()
app.include_router(item_Rob)
