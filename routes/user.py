from fastapi import FastAPI, Depends, HTTPException, status,APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from fastapi import FastAPI, Form
import jwt
#database connection
from config.db import conn

from models.index import user
from passlib.context import CryptContext
from schemas.item import user_class


user_obj=APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
JWT_SECRET='my_secret'
@user_obj.post("/user")
async def create_user(form_data: user_class= Depends()):
    print(type(form_data))
    conn.execute(user.insert().values(       
         First_Name=form_data.First_Name,
         Last_Name=form_data.Last_Name,
         username=form_data.username,     
         password_hash=pwd_context.hash(form_data.password_hash)
         ))
    return form_data


def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
         
async def authenticate_user(username: str, password: str):
    userf=conn.execute(user.select().where (user.c.username==username))
    if not userf:
        return False 
    d, a = {}, []
    for rowproxy in userf:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)
    a=a[0]    
    hash=a["password_hash"]
    if not pwd_context.verify(password,hash):
        return False   
    return True

@user_obj.post("/User Login")
async  def login(form_data: OAuth2PasswordRequestForm = Depends()):
      if(await authenticate_user(form_data.username, form_data.password)):
        return "Access Granted"
      else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Invalid username or password'
        )



