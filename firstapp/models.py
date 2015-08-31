from django.db import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, create_engine

Base = declarative_base()
dbsession = None

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    age = Column(Integer())
    phone = Column(String(11))
    email = Column(String(100))
    
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    def __repr__(self):
        return "<User('%S', '%s', '%s', '%s')>" % (self.name, str(self.age), self.phone, self.email)

def connect_db():
    engine = create_engine('mysql://root:123456@127.0.0.1:3306/python', echo=True)
    metadata = MetaData()
    Session = sessionmaker(bind=engine)
    global dbsession
    dbsession = Session()

def add_record(record):
    global dbsession
    dbsession.add(record)
 
def update_db():
    global dbsession
    dbsession.commit()
    
