from models import  User, Income, Expense, Category, Budget, session,database
from models.database import Base
from datetime import datetime
from sqlalchemy import func
def add_user():
    username = input('Enter username: ')
    email = input('Enter email: ')
    password_hash = input('Enter password: ')
    new_user = User(username=username, email=email, password_hash=password_hash)
    try:
        session.add(new_user)
        session.commit()
        print(f"User {username} added successfully.")
    except Exception as e:
        session.rollback()
        if 'unique constraint' in str(e).lower():
            print('Error: This username or email already exist.')
        else:
            print('An expected error occoured:', e)    

def list_users():
    users = session.query(User).all()
    if not users:
        print('No users found.')
    else:
        for user in users:
            print(user)    

def update_user(user_id, username=None, email=None, password_hash=None):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        if username is not None:
            user.username = username
        if email is not None:
            user.email = email
        if password_hash is not None:
            user.password_hash = password_hash
        session.commit()
        print(f'User {user_id} updated successfully.')  
    else:
        print(f'user {user_id} not found.')    

def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f'User {user_id} deleted successfully.')
    else: 
        print(f'User {user_id} not found.')    

def add_income():
    user_id = int(input('Enter user ID: '))
    source = input('Enter income source: ')
    amount = float(input('Enter income amount: '))
    date_str = input('Enter income date (YYYY-MM-DD): ')
    date = datetime.strptime(date_str,'%Y-%m-%d').date()
    new_income = Income(user_id=user_id, source=source, amount=amount, date=date)
    session.add(new_income)
    session.commit()
    print(f"Income from {source} added successfully.")

def list_incomes():
    incomes = session.query(Income).all()
    if not incomes:
        print('No incomes available.')
    else: 
        for income in  incomes:
            print(income)
def update_income(income_id, source=None, amount=None, date=None):
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        if source is not None:
            income.source = source
        if amount is not None:
            income.amount = amount
        if date is not None:
            income.date = date
        session.commit()
        print(f'Income {income_id} is updated successfuly.')
    else:
        print(f'Income {income_id} not found.')                        

def delete_income(income_id):
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        session.delete(income)
        session.commit()
        print(f'Income {income_id} deleted successfully.')
    else:
        print(f'Income {income_id} not found.')        
def add_expense():
    user_id = int(input('Ebter user ID: '))
    category_id = int(input('Enter category ID: '))
    amount = float(input('Enter expense amount: '))
    date_str = input('Enter expense date (YYYY-MM-DD): ')
    date = datetime.strptime(date_str,'%Y-%m-%d').date()
    description = input('Enter expense description: ')
    new_expense = Expense(user_id=user_id, category_id=category_id, amount=amount, date=date, description=description)
    session.add(new_expense)
    session.commit()
    print(f"Expense {description} added successfully.")

def list_expenses():
    expenses =  session.query(Expense).all()
    if not expenses:
        print('No expenses found.')
    else:
        for expense in expenses:
            print(expense)   

def update_expense(expense_id, category_id=None, amount= None, date=None, description = None):
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        if category_id is not None:
            expense.category_id = category_id
        if amount is not None:
            expense.amount = amount
        if date is not None:
            expense.date  = date
        if description is not None:
            expense.description = description
        session.commit()
        print(f'Expense {expense_id} is updated successfully.')
    else:
        print(f'Expense {expense_id} not found.') 

def delete_expense(expense_id):
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print(f'Expense {expense_id} deleted succesfully.')
    else:
        print(f'Expense {expense_id} not found.')    

def add_category():
    user_id = int(input('Enter user ID: '))
    name= input('Enter category name: ')
    new_category = Category(user_id=user_id,name=name)
    session.add(new_category)
    session.commit()
    print(f"Category {name} added successfully. ")  

def list_categories():
    categories = session.query(Category).all()
    if not categories:
        print('No categories found.')
    else:
        for category in categories:
            print(category)    

def update_category(category_id, name=None, user_id=None):
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        if user_id is not None:
            category.user_id = user_id
        if name is not None:
            category.name = name
        session.commit()
        print(f'Category {category_id} is updated succesfully.')
    else:
        print(f'Category {category_id} not found.')    

def delete_category(category_id):
    category = session.query(Category).filter_by(id= category_id).first()
    if category:
        session.delete(category)
        session.commit()
        print(f'Category {category_id} deleted succesfully.') 
    else:
        print(f'Category {category_id} not found.')       


def add_budget():
    category_id = int(input('Enter Category ID: '))
    amount = float(input('Enter budget amount: '))
    period_start_str = input('Enter period start date (YYYY-MM-DD): ')
    period_start= datetime.strptime(period_start_str,'%Y-%m-%d').date()
    period_end_str = input('Enter period end date (YYYY-MM-DD): ')
    period_end= datetime.strptime(period_end_str,'%Y-%m-%d').date()
    new_budget = Budget(category_id=category_id, amount=amount, period_start=period_start, period_end=period_end)
    session.add(new_budget)
    session.commit()
    print(f"Budget for category ID {category_id} added successfuly.")

def list_budgets():
    budgets = session.query(Budget).all()
    if not budgets:
        print('No budgets found.')
    else:
        for budget in budgets:
            print(budget)    
def check_balance():
    user_id = int(input('Enter user ID to check balance: ')) 

    total_income = session.query(func.sum(Income.amount)).filter(Income.user_id == user_id).scalar() or 0
    total_expenses = session.query(func.sum(Expense.amount)).filter(Expense.user_id == user_id).scalar() or 0  

    budgeted_amount = session.query(func.sum(Budget.amount)).filter(Budget.category_id.in_(
        session.query(Category.id).filter(Category.user_id == user_id)
    )).scalar() or 0           
    
    balance = total_income - total_expenses

    return total_income, total_expenses, balance, budgeted_amount

def display_balance():
    total_income, total_expenses, balance, budgeted_amount = check_balance()
    
    print(f"Total income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Your Balance is: ${balance}")
    print(f"Total Budgeted Amount: {budgeted_amount}")

    if budgeted_amount > balance:
        print('Warning: Your expenses exceed your budget!')
    else:
        print('Your expenses are within your budget.')
   

def update_budget(budget_id, category_id = None, amount=None,period_start =None, period_end = None):
    budget = session.query(Budget).filter_by(id=budget_id).first()
    if budget:
        if category_id is not None:
            budget.category_id = category_id
        if amount is not None:
            budget.amount = amount
        if period_start is not None:
            budget.period_start = period_start
        if period_end is not None:
            budget.period_end = period_end
        session.commit()
        print(f'Budget {budget_id} updated successfully.')
    else:
        print(f'Budget {budget_id} not found.') 

def delete_budget(budget_id):
    budget = session.query(Budget).filter_by(id= budget_id).first()
    if budget:
        session.delete(budget)
        session.commit()
        print(f'Budget {budget_id} deleted successfully.')
    else:
        print(f'Budget {budget_id} not found.')    




def main():
    while True:
        print("\n==== Personal Budget Tracker ====")
        print("1. Users")
        print("2. Incomes")
        print("3. Expenses")
        print("4. Categories")
        print("5. Budgets")
        print("6. Check Balance")
        print("7. Exit")

        choice = input("Select your choice (1-7): ")

        if choice == '1':
            while True:
                print("\n--- User Management ---")
                print("1. Add User")
                print("2. List Users")
                print("3. Update User")
                print("4. Delete User")
                print("5. Back to Main Menu")

                user_choice = input("Select your choice (1-5): ")
                
                if user_choice == '1':
                    add_user()
                elif user_choice == '2':
                    list_users()
                elif user_choice == '3':
                    user_id = int(input('Enter user ID to update: '))
                    username = input('Enter new username (leave blank to keep current): ') or None
                    email = input('Enter new email (leave blank to keep current): ') or None
                    password_hash = input('Enter new password hash (leave blank to keep current): ') or None
                    update_user(user_id, username, email, password_hash)
                elif user_choice == '4':
                    user_id = int(input('Enter user ID to delete: '))
                    delete_user(user_id)
                elif user_choice == '5':
                    break
                else:
                    print('Invalid choice. Please enter number between 1 and 5')

        elif choice == '2':
            while True:
                print("\n--- Income Management ---")
                print("1. Add Income")
                print("2. List Incomes")
                print("3. Update Income")
                print("4. Delete Income")
                print("5. Back to Main Menu")

                income_choice = input("Select your choice (1-5): ")

                if income_choice == '1':
                    add_income()
                elif income_choice == '2':
                    list_incomes()
                elif income_choice == '3':
                    income_id = int(input('Enter income ID to update: '))
                    source = input('Enter new source (leave blank to keep current): ') or None
                    amount = input('Enter new amount (leave blank to keep current): ') or None
                    amount = float(amount) if amount else None
                    date_str = input('Enter new date (leave blank to keep current): ') or None
                    date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None
                    update_income(income_id, source, amount, date)
                elif income_choice == '4':
                    income_id = int(input('Enter income ID to delete: '))
                    delete_income(income_id)
                elif income_choice == '5':
                    break
                else:
                    print('Invalid choice. Please enter number between 1 and 5')

        elif choice == '3':
            while True:
                print("\n--- Expense Management ---")
                print("1. Add Expense")
                print("2. List Expenses")
                print("3. Update Expense")
                print("4. Delete Expense")
                print("5. Back to Main Menu")

                expense_choice = input("Select your choice (1-5): ")

                if expense_choice == '1':
                    add_expense()
                elif expense_choice == '2':
                    list_expenses()
                elif expense_choice == '3':
                    expense_id = int(input('Enter expense ID to update: '))
                    category_id = int(input('Enter new category ID (leave blank to keep current): ') or None)
                    amount = input('Enter new amount (leave blank to keep current): ') or None
                    amount = float(amount) if amount else None
                    date_str = input('Enter new date (leave blank to keep current): ') or None
                    date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None
                    description = input('Enter new description (leave blank to keep current): ') or None
                    update_expense(expense_id, category_id, amount, date, description)
                elif expense_choice == '4':
                    expense_id = int(input('Enter expense ID to delete: '))
                    delete_expense(expense_id)
                elif expense_choice == '5':
                    break
                else:
                    print('Invalid choice. Please enter number between 1 and 5')

        elif choice == '4':
            while True:
                print("\n--- Category Management ---")
                print("1. Add Category")
                print("2. List Categories")
                print("3. Update Category")
                print("4. Delete Category")
                print("5. Back to Main Menu")

                category_choice = input("Select your choice (1-5): ")

                if category_choice == '1':
                    add_category()
                elif category_choice == '2':
                    list_categories()
                elif category_choice == '3':
                    category_id = int(input('Enter category ID to update: '))
                    name = input('Enter new name (leave blank to keep current): ') or None
                    update_category(category_id, name)
                elif category_choice == '4':
                    category_id = int(input('Enter category ID to delete: '))
                    delete_category(category_id)
                elif category_choice == '5':
                    break
                else:
                    print('Invalid choice. Please enter number between 1 and 5')

        elif choice == '5':
            while True:
                print("\n--- Budget Management ---")
                print("1. Add Budget")
                print("2. List Budgets")
                print("3. Update Budget")
                print("4. Delete Budget")
                print("5. Back to Main Menu")

                budget_choice = input("Select your choice (1-5): ")

                if budget_choice == '1':
                    add_budget()
                elif budget_choice == '2':
                    list_budgets()
                elif budget_choice == '3':
                    budget_id = int(input('Enter budget ID to update: '))
                    category_id = input('Enter new category ID (leave blank to keep current): ') or None
                    category_id = int(category_id) if category_id else None
                    amount = input('Enter new amount (leave blank to keep current): ') or None
                    amount = float(amount) if amount else None
                    period_start_str = input('Enter new period start date (leave blank to keep current): ') or None
                    period_start = datetime.strptime(period_start_str, '%Y-%m-%d').date() if period_start_str else None
                    period_end_str = input('Enter new period end date (leave blank to keep current): ') or None
                    period_end = datetime.strptime(period_end_str, '%Y-%m-%d').date() if period_end_str else None
                    update_budget(budget_id, category_id, amount, period_start, period_end)
                elif budget_choice == '4':
                    budget_id = int(input('Enter budget ID to delete: '))
                    delete_budget(budget_id)
                elif budget_choice == '5':
                    break
                else:
                    print('Invalid choice. Please enter number between 1 and 5')

        elif choice == '6':
            display_balance()
        elif choice == '7':
            print('Thank you for managing your budget!')
            break
        else:
            print('Invalid choice. Please enter number between 1 and 7')
 


