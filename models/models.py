from sqlalchemy import Column, String, Date, Integer, Float, ForeignKey,create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key= True)
    username = Column(String, nullable = False)
    email = Column(String, unique= True, nullable =False)
    password_hash = Column(String, nullable=False)
    
    incomes = relationship('Income', back_populates='user')
    expenses = relationship('Expense', back_populates='user')

class Income(Base):
    __tablename__ = 'incomes'    
    id = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey('users.id'))
    source = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    user = relationship('User', back_populates='incomes')

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=False)

    user =  relationship('User', back_populates='expenses') 
    category = relationship('Category', back_populates='expenses') 

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    expenses = relationship('Expense', back_populates='category')
    budgets = relationship('Budget', back_populates='category')

class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id')) 
    amount = Column(Float, nullable=False) 
    period_start = Column(Date, nullable=False)
    period_end = Column(Date, nullable=False)

    category = relationship('Category', back_populates='budgets')

Database_url  = 'sqlite:///budget_tracker.db'
engine  =create_engine(Database_url)   
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()
    