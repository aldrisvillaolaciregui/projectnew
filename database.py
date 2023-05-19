from peewee import *
from database import MySQLDatabase


database=MySQLDatabase(
    "inventario-reparaciones",
    user="root",
    password="",
    host="localhost",
    port=3306
)

class usuarios(Model):
    username=TextField(unique=True)
    password=TextField()
    class Meta:
        database=database
        
        
database.create_tables([usuarios])