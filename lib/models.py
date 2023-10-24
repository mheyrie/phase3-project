#!/usr/bin/env python3

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_no = Column(Integer, nullable=True)

    cars = relationship('Car', back_populates='owner')

    def __init__(self, first_name, last_name, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no

    def __repr__(self):
        return f"{self.id}, " + \
            f"{self.first_name}, " + \
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
    plate_no = Column(Integer, nullable=True)
    created = Column(DateTime, default=datetime.utcnow)
        
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
        
    owner = relationship('Owner', back_populates='cars')


    def __init__(self, car_brand, color, production_year, plate_no, owner_id):
        self.car_brand = car_brand
        self.color = color
        self.production_year = production_year
        self.plate_no = plate_no
        self.owner_id = owner_id
        

    def __repr__(self):
        return f"{self.id}, " + \
            f"Car Brand: {self.car_brand}, Car color:{self.color}" + \
            f"Year: {self.production_year}, Plate no:{self.plate_no}" + \
            f"{self.owner_id}"



# owner1 = Owner(
#     first_name="Mary", last_name="MaryMAry",
#     phone_no=123456789
# )

# owner2 = Owner(
#     first_name="Owen", last_name="Oweeeeen",
#     phone_no=23456789
# )

# owner3 = Owner(
#     first_name="Moses", last_name="Oyeeee",
#     phone_no=45637255
# )
# owner4 = Owner(
#     first_name="Johnny", last_name="Ola",
#     phone_no=123456789
# )
# owner5 = Owner(
#     first_name="Feyi", last_name="Tee",
#     phone_no=12345678
# )



engine = create_engine("sqlite:///data.db", echo=True)
Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()