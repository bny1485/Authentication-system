
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    email_addr = db.Column(db.String(80), nullable=False, unique=True)
    email_addr_is_Confirm = db.Column(db.Boolean)
    phone_number = db.Column(db.String(80), nullable=False, unique=True)
    phone_number_is_Confirm = db.Column(db.Boolean)
    password = db.Column(db.String(80), nullable=False, unique=True)

    def __repr__(self):
        return f'{id}, {name}, {username}, {email_addr}:{email_addr_is_Confirm}, {phone_number}:{phone_number_is_Confirm}'