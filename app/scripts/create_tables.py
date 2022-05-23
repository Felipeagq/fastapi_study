from app.models.user_model import User
from app.utils.db import db

def create_tables():
    with db:
        db.create_tables(User)