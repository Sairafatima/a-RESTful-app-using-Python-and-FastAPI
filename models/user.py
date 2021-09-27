from sqlalchemy import table, column
from sqlalchemy.sql.schema import PrimaryKeyConstraint, Table
from sqlalchemy.sql.sqltypes import Date, Integer, String
from sqlalchemy import Table,Column
from config.db import meta
#users table#
user = Table(
    'user',meta,
    Column('id',Integer,autoincrement=True),
    Column('First_Name',String(255)),
    Column('Last_Name',String(255)),
    Column('username',String,primary_key=True),
    Column('password_hash',String(255)),
    
)