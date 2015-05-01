from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import  scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound

session = None

# basic
#
def configure(database_uri):
    global session

    engine = create_engine(database_uri)
    session = scoped_session(sessionmaker(bind=engine))
    Base.query = session.query_property()
    #To create all tables, uncomment the below line.
    Base.metadata.create_all(bind=engine)
def commit():
    global session
    session.commit()

def remove_session():
    global session
    return session.remove()
