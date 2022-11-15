import os
from mysql.connector import connect, Error
from dotenv import load_dotenv
load_dotenv()


try:
    with connect(
        host="localhost",
        user=os.getenv("ROOT_USER"),
        password=os.getenv("ROOT_PASSWORD"),
    ) as connection:
        create_database_query = f"CREATE DATABASE {os.getenv('NEW_DATABASE')}"
        with connection.cursor() as cursor:
            res = cursor.execute(create_database_query)
            print(res)
        create_user_query = f"CREATE USER '{os.getenv('NEW_DATABASE')}'@'localhost' IDENTIFIED BY '{os.getenv('NEW_PASSWORD')}'"
        with connection.cursor() as cursor:
            res = cursor.execute(create_user_query)
            print(res)
        grant_privileges_query = f"GRANT ALL PRIVILEGES ON {os.getenv('NEW_DATABASE')}.* TO '{os.getenv('NEW_DATABASE')}'@'localhost'"
        with connection.cursor() as cursor:
            res = cursor.execute(grant_privileges_query)
            print(res)
except Error as e:
    print(e)
    exit()


