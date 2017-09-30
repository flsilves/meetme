import os
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

current_dir = os.path.dirname(os.path.abspath(__file__))
DB_URI = 'sqlite:///' + current_dir + '/main.db'


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)


class Meeting(Base):
    __tablename__ = 'meetings'

    id = Column(Integer, primary_key=True)
    owner = Column(String(255))
    recording = Column(String(255))
    privacy = Column(String(255))


if __name__ == "__main__":
    db = create_engine(DB_URI)
    Base.metadata.drop_all(db)
    Base.metadata.create_all(db)