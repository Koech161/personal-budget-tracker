from models import Base, User, Income, Expense, Category, Budget, session, Database_url

def add_user():
    username = input('Enter username: ')
    email = input('Enter email: ')
    password_hash = input('Enter password: ')
    new_user = User(username=username, email=email, password_hash=password_hash)
    session.add(new_user)
    session.commit()
    print(f"User '{username}' added successfully.")

def list_users():
    users = session.query(User).all()
    if not users:
        print('No users found.')
    else:
        for user in users:
            print(user)    

def add_income():
    user_id = int(input('Enter user ID: '))
    source = input('Enter income source: ')
    amount = float(input('Enter income amount: '))
    date = input('Enter income date (YYYY-MM-DD): ')
    new_income = Income(user_id=user_id, source=source, amount=amount, date=date)
    session.add(new_income)
    session.commit()
    print(f"Income from '{source}' added successfully.")

def list_incomes():
    incomes = session.query(Income).all()
    if not incomes:
        print('No incomes available.')
    else: 
        for income in  incomes:
            print(income)

def add_expense():
    user_id = int(input('Ebter user ID: '))
    category_id: int(input('Enter category ID: '))
    amount = float(input('Enter expense amount: '))
    date = input('Enter expense date (YYYY-MM-DD): ')
    description = input('Enter expense description: ')
    new_expense = Expense(user_id=user_id, category_id=category_id, amount=amount, date=date, description=description)
    session.add(new_expense)
    session.commit()
    print("Expense '{description}' added successfully.")

def list_expenses():
    expenses =  session.query(Expense).all()
    if not expenses:
        print('No expenses found.')
    else:
        for expense in expenses:
            print(expense)     

def add_category():
    name= input('Enter category name: ')
    new_category = Category(name=name)
    session.add(new_category)
    session.commit()
    print("Category '{name}' added successfully. ")  

def list_categories():
    categories = session.query(Category).all()
    if not categories:
        print('No categories found.')
    else:
        for category in categories:
            print(category)        

def add_budget():
    category_id = int(input('Enter Category ID: '))
    amount = float(input('Enter budget amount: '))
    period_start = input('Enter period start date (YYYY-MM-DD): ')
    period_end = input('Enter period end date (YYYY-MM-DD): ')
    new_budget = Budget(category_id=category_id, amount=amount, period_start=period_start, period_end=period_end)
    session.add(new_budget)
    session.commit()
    print(f"Budget for category ID '{category_id}' added successfuly.")

def list_budgets():
    budgets = session.query(Budget).all()
    if not budgets:
        print('No budgets found.')
    else:
        for budget in budgets:
            print(budget)       


def main():
    while True:
        print("\n====Personal_Budget_Tracker")
        print("1. Add User")
        print("2. List Users")
        print("3. Add Income")
        print("4. List incomes")
        print("5. Add Expense")
        print("6. List Expenses")
        print("7. Add Category")
        print("8. List Categories")
        print("9. Add Budget")
        print("10. List Budgets")
        print("11. Exit")

        choice = input("Enter your Choice (1 - 11)")

        if choice == '1':
            add_user()
        elif choice == '2':
            list_users()
        elif choice == '3':
            add_income()        
        elif choice == '4':
            list_incomes()   
        elif choice == '5':
            add_expense()
        elif choice == '6':
            list_expenses()
        elif choice == '7':
            add_category()
        elif choice == '8':
            list_categories()    
        elif choice == '9':
            add_budget()
        elif choice == '10':
            list_budgets()
        elif choice == '11':
            print('Thank you for managing your budget')
            break
        else:
            print('Invalid choice. Please enter number between 1 and 11')  

if __name__ == '__main__':
    main()             

