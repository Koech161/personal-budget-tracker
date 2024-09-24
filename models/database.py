from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Database_url = 'sqlite:///budget_tracker.db'
engine = create_engine(Database_url)   
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
