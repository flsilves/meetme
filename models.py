import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

current_dir = os.path.dirname(os.path.abspath(__file__))
DB_URI = 'sqlite:///' + current_dir + '/main.db'

Base = declarative_base()


class Permission(Base):
    __tablename__ = 'permissions'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    recording_id = Column(Integer, ForeignKey('recordings.id'), primary_key=True)


class Recording(Base):
    __tablename__ = 'recordings'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    storage_url = Column(String(255), unique=True)
    password = Column(String(255))



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    association = relationship('Recording', secondary='permissions', backref='users', cascade='save-update, merge, delete')


if __name__ == '__main__':
    db = create_engine(DB_URI)
    Base.metadata.drop_all(db)
    Base.metadata.create_all(db)
