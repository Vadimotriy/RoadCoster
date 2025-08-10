import datetime

from sqlalchemy import create_engine, Column, Float, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///costing.db')
Base = declarative_base()

class Prices(Base):
    __tablename__ = 'prices'

    time = Column(String, default=datetime.datetime.now().strftime("%d.%m %H:%M:%S"), primary_key=True)
    price = Column(Float, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
