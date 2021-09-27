from fastapi import FastAPI
from routes.index import item_Rob
from routes.user import user_obj
from schemas.item import user_class
import jwt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import bcrypt
from passlib.context import CryptContext
from tortoise import fields 
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model 
from schemas.item import user_class
from schemas.index import Item_class
from models.Items import item_table,user,UserIn
from config.db import conn
app=FastAPI()
