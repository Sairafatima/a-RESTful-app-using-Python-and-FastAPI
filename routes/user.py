from fastapi import FastAPI, Depends, HTTPException, status,APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from passlib.context import CryptContext
from fastapi import FastAPI, Form
import jwt
#database connection
from config.db import conn

from models.index import user
from schemas.item import user_class

user_obj=APIRouter() 
#variable for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#defining OAuth2PasswordBearer object with token url which is a dummy url in this impelementation
#this TokenURl will change according to requirements like generating tokens for user auth
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
#for token creation :not used in the code below
JWT_SECRET='my_secret'

#create/register users in databse
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

#
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


async def authenticate_user(username: str, password: str):
    userf=conn.execute(user.select().where (user.c.username==username))
    #if username not found 
    if not userf:
        return False 
    #this code change the table result into actual dict list
    d, user_list = {}, []
    for rowproxy in userf:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        user_list.append(d)
    user_dict=user_list[0]    
    #get the value of password_hash for specific user
    hash=user_dict["password_hash"]
    #verify password
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



