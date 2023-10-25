#!/usr/bin/env python3

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base




Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_no = Column(Integer, nullable=True)

    cars = relationship('Car', back_populates='owner')

   
    def __repr__(self):
        return f"{self.first_name}, " + \
            f"{self.last_name}, " + \
            f"{self.phone_no}"
    
    def full_name(self):
        return f"Fullname: {self.first_name} {self.last_name}"






class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    car_brand = Column(String, nullable=False)
    color = Column(String, nullable=True)
    production_year = Column(Integer, nullable=False)
    plate_no = Column(String, nullable=True)
    created = Column(DateTime, default=datetime.utcnow)
        
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
        
    owner = relationship('Owner', back_populates='cars')

    def __repr__(self):
        return f"Car Brand: {self.car_brand}, Car color: {self.color} " + \
            f"Year: {self.production_year}, Plate no:{self.plate_no}" + \
            f"{self.owner_id}"


engine = create_engine("sqlite:///data.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()



