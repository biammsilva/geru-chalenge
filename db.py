from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Session(Base):
    id = Column(Integer, primary_key=True)
    content = Column(String)
    created_at = Column(DateTime)
    page = Column(String)
    session_id = Column(String)


engine = create_engine('sqlite:///teste-geru.db', echo=True)
Base.metadata.create_all(engine)
