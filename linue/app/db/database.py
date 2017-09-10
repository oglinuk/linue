'''
linue database

Database for the website
'''

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

def getDBEngine():
    # Interface to the database with SQLAlchemy
    engine = create_engine('mysql://root:ad46ws85qe79@localhost:3306/webdb')
    return engine

def getDBConnection():
    connection = getDBEngine()
    return connection

def getDBSession():
    Session = sessionmaker()
    Session.congifure(bind=getDBEngine())
    session = Session()
    return session

def getDBMetaData():
    meta = MetaData()
    return meta

def getDBTable(prTable):
    dbTable = Table(prTable, getDBMetaData(), autoload=True, autoload_with=getDBEngine())
    return dbTable
