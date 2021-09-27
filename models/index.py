#this file creates abrstraction between actual impelemtaion and object calling
from sqlalchemy import MetaData
from models.Items import item_table
from models.user import user
meta =MetaData()