# 2015

from sqlalchemy import Column, ForeignKey, Integer,Float, String,UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Profile(Base):

    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    number = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    company = Column(String, nullable=False)
    title = Column(String, nullable=False)

    def as_dict(self):
        res = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return res

    def __repr__(self):
        s = "<Profile(id='{0}', name='{1}', company='{2})'>"
        return s.format(self.id, self.name, self.company)

    def __init__(self, name, number, address, company, title):
        self.name = name
        self.number = number
        self.address = address,
        self.company = company,
        self.title = title

class Weekend(Base):

    __tablename__ = "weekend"
    id = Column(Integer, primary_key=True)
    week_of = Column(Date, nullable=False)
    place = Coulmn(String, nullable=False)

    def as_dict(self):
        res = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return res

    def __repr__(self):
        s = "<Weekend(id='{0}', week_of'{1}', place='{2})'>"
        return s.format(self.id, self.week_of, self.place)

    def __init__(self):
        self.week_of = week_of
        self.place = place


class Participants(Base):

    __tablename__ = "participants"
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey("profile.id", ondelete="CASCADE"))
    weekend_id = Column(Integer, ForeignKey("weekend.id", ondelete="CASCADE"))

    #Constraint
    UniqueConstraint('profile_id', 'weekend_id')

    def as_dict(self):
        res = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return res

    def __repr__(self):
        s = "<Participants(id='{0}', profile_id='{1}', weekend_id='{2})'>"
        return s.format(self.id, self.profile_id, self.weekend_id)

    def __init__(self, profile_id, weekend_id):
        self.profile_id = profile_id
        self.weekend_id = weekend_id

class Expenses(Base):

    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    weekend_id = Column(Integer, ForeignKey("weekend.id", ondelete="CASCADE"))
    expense_type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    profile_id = Column(Integer, ForeignKey("profile.id", ondelete="CASCADE"))
    date = Column(Date, nullable=False)

    def as_dict(self):
        res = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return res

    def __repr__(self):
        s = "<Expenses(id='{0}', weekend_id='{1}', expense_type='{2})', amount='{3}', profile_id='{4}'>"
        return s.format(self.id, self.weekend_id, self.expense_type, self.amount, self.profile_id)

    def __init__(self, profile_id, weekend_id, expense_type, date, amount):
        self.profile_id = profile_id
        self.weekend_id = weekend_id
        self.expense_type = expense_type
        self.amount = amount
        self.date = date


    
