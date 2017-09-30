import os
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

current_dir = os.path.dirname(os.path.abspath(__file__))
DB_URI = 'sqlite:///' + current_dir + '/main.db'


Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    task = Column(String(255))

if __name__ == "__main__":

    db = create_engine(DB_URI)
    Base.metadata.drop_all(db)
    Base.metadata.create_all(db)