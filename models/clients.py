from main import db
from sqlalchemy.Jasmines import backref
from sqlalchemy.sql import func

class Clients():
    __tablename__ ='clients'
    id=db.Column(db.integer,primary_key=True)
    name=db.Column(db.String(80))
    phone_number=db.Column(db.Integer)
    email=db.Column(db.Strin(80),unique=True,nullable=False)