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

#profile

def post_profile(name,address,number,company,title):
    if Profile.query.filter_by(name=name).count() == 0:
        profile = Profile(name=name,address=address,number=number,
                            title=title, company=company)
        session.add(profile)
        return True, profile
    return False, None

def get_profile(profile_id=None):
    if profile_id:
        try:
            return True, Profile.query.filter_by(id=profile_id).one()
        except NoResultFound:
            return False, None
    else:
        return True, Profile.query.all()


def del_profile(profile_id):
    if Profile.query.filter_by(id=profile_id).count() == 1:
        profile = Profile.query.filter_by(id=profile_id).one()
        session.delete(profile)
        return True
    return False

#weekend
def post_weekend(week_of, place):
    if Weekend.query.filter_by(week_of=week_of).count() == 0:
        weekend = Weekend(week_of=week_of, place=place)
        session.add(weekend)
        return True, weekend
    return False, None

def get_weekend(weekend_id=None):
    if weekend_id:
        try:
            return True, Weekend.query.filter_by(id=weekend_id).one()
        except NoResultFound:
            return False, None
    else:
        return True, Weekend.query.all()

def del_weekend(weekend_id):
    if Weekend.query.filter_by(id=weekend_id).count() == 1:
        weekend =  Weekend.query.filter_by(id=weekend_id).one()
        session.delete(weekend)
        return True
    return False

#participants
def post_participants(weekend_id, profile_id):
    if Participants.query.filter_by(weekend_id=weekend_id).filter_by(profile_id=profile_id).count() == 0:
        participants = Participants(weekend_id=weekend_id, profile_id=profile_id)
        session.add(participants)
        return True, participants
    return False, None

def get_participants(weekend_id=None,participant_id=None):
    if weekend_id:
        try:
            participants = Participants.query.filter_by(weekend_id=weekend_id).all()
            return True, participants
        except NoResultFound:
            return False, None
    elif participant_id:
        try:
            participants = Participants.query.filter_by(id=participant_id).one()
            return True, participants
        except NoResultFound:
            return False, None
    else:
        return True, Participants.query.all()

def del_participant(participant_id):
    if Participant.query.filter_by(id=participant_id).count() == 1:
        participant = articipant.query.filter_by(id=participant_id).one()
        session.delete(participant)
        return True
    return False

#Expenses
def post_expenses():

def get_expenses():

def delete_expenses():
