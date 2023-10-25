
# Phase3-Python-project(Car wash register)

This project was designed to cater for car wash register, where there will be a record for every car brought in for washing and the details of the owner will also be recorded along side some of the information about the car for easy identification.

# Project setup and design of the layout
-Create a folder for the project in your directory, navigate into the folder and also create a new repository on github, then follow the instruction to link the both files together. Ensure the repositoryis set to Public. If this is done right you should get an empty READme file along

# Installation of dependecies
* These are most of the dependecies i installed for this project
 -pipenv installed
 -pipenv shell
 -Installation of sqlaclchemy
 -Installation of almebic
 -Installation of Click

    [packages]
    sqlalchemy = "*"
    alembic = "*"
    click = "*"
You should see something like this in your Pipfile

 # files setup
 - importing of the required dependecies in my file for the project
    
    [import]

    from datetime import datetime

    from sqlalchemy import Column, Integer, String, 
    DateTime, create_engine, ForeignKey

    from sqlalchemy.orm import relationship, sessionmaker

    from sqlalchemy.ext.declarative import declarative_base

# Project
-created the model for my project where i have two class(Owner and Car) defined there and also assigned the Base class, session and engine in the models.py file.

- Created the structure for my database table, i implemented one-to-many relationship between the two tables.

- I also have another file mycalc.py where i implemented the CLI program and also added to query functionality to my project.

