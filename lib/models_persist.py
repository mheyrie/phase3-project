#!/usr/bin/env python3

from datetime import datetime
from models import Owner, Car, engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

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

# session.add_all([owner1, owner2, owner3, owner4, owner5])

# owner7 = Owner(
#     first_name="Harrison", last_name="Ojah",
#     phone_no=35644888
# )



car6 = Car(car_brand="Toyota", color="Black", production_year=2022, plate_no=111, owner_id=2)
car4 = Car(car_brand="Ferari", color="Grey", production_year=2024, plate_no=555, owner_id=5)
car5 = Car(car_brand="BMW", color="Black", production_year=2023, plate_no=1414, owner_id=6)


# car1 = Car(car_brand="Highlander", color="Blue", production_year=2020, plate_no=555, owner=owner6)
# car2 = Car(car_brand="BMW", color="Red", production_year=2018, plate_no=111, owner=owner6)
session.add_all([car6, car4, car5])
session.commit()
