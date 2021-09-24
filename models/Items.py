from sqlalchemy import table, column
from sqlalchemy.sql.schema import PrimaryKeyConstraint, Table
from sqlalchemy.sql.sqltypes import Date, Integer, String
from sqlalchemy import Table,Column
from config.db import meta
item_table = Table(
    'Items',meta,
    Column('id',Integer,primary_key=True),
    Column('Name',String(255)),
    Column('Location',String(255)),
    Column('Description',String(1000)),
    Column('Date',Date),
    Column('others',String(1000))
)