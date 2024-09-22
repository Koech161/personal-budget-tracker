# personal-budget-tracker
- This application simplifies the tracking and management of user personal finances, helping user to stay on top of budget.

# Run the folllowing commands
1. git clone this repository
2. pipinv install
3. pipenv shell
4. pip install alembic sqlalchemy
5. after creating tables run alembic init alembic
6. alembic revison --autogenerate -m 'initial migration'
7. alembic upgrade head
8. on the virtual enviroment run # python app.py 

## Features
1. Users can add : - user
                   - income
                   - budgets
                   - budget category
                   - expenses
2. Users can list:  - users
                    - incomes
                    - budgets
                    - catagories
                    - expenses
3. Users can  update: - users
                     - income
                     - budgets     
                     - categories
                     - expenses
4. User can delete  user, income, budgets, categories and expenses by ID
5. A CLI is availablefor execcuting commands for adding, listing, deleting and updating.                                                             