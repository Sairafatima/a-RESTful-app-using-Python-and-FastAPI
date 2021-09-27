from re import M
from sqlalchemy import create_engine,MetaData
#this file impelments database connection and configrations
engine=create_engine("mysql+pymysql://root@localhost:3306/test") 
meta=MetaData()
conn=engine.connect()