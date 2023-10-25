import click
from models import Owner, Car, session, Base, engine

@click.command()
@click.option('--first_name', prompt='Enter First Name')
@click.option('--last_name', prompt='Enter Last Name')
@click.option('--phone_no', prompt='Phone Number')
@click.option('--car_brand', prompt='Enter Car Brand')
@click.option('--color', prompt='Enter Car Color')
@click.option('--production_year', prompt='Enter Car Production Year')
@click.option('--plate_no', prompt='Enter Car Plate no')
@click.option('--owner_id', prompt='Enter Owner ID')

def owner_reg(first_name,last_name,phone_no, car_brand, color, production_year, plate_no, owner_id):
    customer = Owner(
        first_name = first_name,
        last_name = last_name,
        phone_no = phone_no
    )
    customer_car = Car(
        car_brand = car_brand,
        color = color,
        production_year = production_year,
        plate_no = plate_no,
        owner_id = owner_id       
    )

    session.add(customer)
    session.add(customer_car)
    session.commit()


if __name__=="__main__":
    owner_reg()
    