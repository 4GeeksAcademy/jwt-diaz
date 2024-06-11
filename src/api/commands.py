
import click
from api.models import db, User

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator.
Flask commands are useful to run cronjobs or tasks outside of the API but still in integration 
with your database. For example: Import the price of bitcoin every night at 12am.
"""

def setup_commands(app):

    @app.cli.command("insert-test-users")
    @click.argument("count")
    def insert_test_users(count):
        """
        Insert a specified number of test users into the database.
        
        Usage: flask insert-test-users <count>
        """
        try:
            count = int(count)
        except ValueError:
            print("Error: count must be an integer.")
            return

        if count <= 0:
            print("Error: count must be a positive integer.")
            return

        print("Creating test users...")
        for x in range(1, count + 1):
            user = User(
                email=f"test_user{x}@test.com",
                password="123456",
                is_active=True
            )
            db.session.add(user)
            db.session.commit()
            print(f"User: {user.email} created.")

        print("All test users created.")

    @app.cli.command("insert-test-data")
    def insert_test_data():
        """
        Placeholder command to insert test data into the database.
        
        Usage: flask insert-test-data
        """
        print("Insert test data command is not implemented yet.")
