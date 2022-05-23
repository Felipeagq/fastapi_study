import peewee
from app.utils.db import db

class User(peewee.Model):
    email = peewee.Charfield(unique=True, index=True)
    username = peewee.Charfield(unique=True, index=True)
    email = peewee.Charfield()
    
    class Meta:
        database = db