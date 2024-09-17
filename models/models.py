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

    def __repr__(self):
        return f'User(id={self.id},' + \
            f'username={self.username},' + \
            f'email={self.email})'

class Income(Base):
    __tablename__ = 'incomes'    
    id = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey('users.id'))
    source = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    user = relationship('User', back_populates='incomes')

    def __repr__(self):
        return f'Income(id={self.id},' + \
            f'source={self.source},' + \
            f'amount={self.amount},' + \
            f'date={self.date})'

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

    def __repr__(self):
        return f'Expense(id={self.id},' + \
            f'amount={self.amount},' + \
            f'date={self.date},' + \
            f'description={self.description})'

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    expenses = relationship('Expense', back_populates='category')
    budgets = relationship('Budget', back_populates='category')

    def __repr__(self):
        return f'Category(id={self.id},' + \
            f'name={self.name},)'

class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id')) 
    amount = Column(Float, nullable=False) 
    period_start = Column(Date, nullable=False)
    period_end = Column(Date, nullable=False)

    category = relationship('Category', back_populates='budgets')

    def __repr__(self):
        return f'Budget(id={self.id},' + \
            f'amount={self.amount},' + \
            f'period_start={self.period_start},' + \
            f'period_end={self.period_end})'

Database_url  = 'sqlite:///budget_tracker.db'
engine  =create_engine(Database_url)   
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()
    