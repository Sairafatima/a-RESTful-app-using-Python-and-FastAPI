from sqlalchemy import table, column
from sqlalchemy.sql.schema import PrimaryKeyConstraint, Table
from sqlalchemy.sql.sqltypes import Date, Integer, String
from sqlalchemy import Table,Column
from config.db import meta
item_table = Table(
    'item_table',meta,
    Column('id',Integer,autoincrement=True, primary_key=True),
    Column('Name',String(255)),
    Column('Location',String(255)),
    Column('Description',String),
    Column('Date',Date),
    Column('others',String)
)

user = Table(
    'user',meta,
    Column('id',Integer,autoincrement=True),
    Column('First_Name',String(255)),
    Column('Last_Name',String(255)),
    Column('username',String,primary_key=True),
    Column('password_hash',String(255)),
    
)
UserIn = Table(
    'UserIn ',meta,

    Column('name',String(255)),

    Column('password_hash',String),
    
)
