# personal-budget-tracker
- This project store and manage personal budgets.

# Run the folllowing commands
1. git clone this repository
2. pipinv install
3. pipenv shell
4. pip install alembic sqlalchemy
5. after creating tables run alembic init alembic
6. alembic revison --autogenerate -m 'initial migration'
7. alembic upgrade head
8. on the virtual enviroment run # python app.py 