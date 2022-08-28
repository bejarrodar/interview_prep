login = "root"
password = "root"
database = "interviewprep"
host='127.0.0.1'


import mysql.connector
from mysql.connector import errorcode

import tables


def create_database():
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host)
        cursor = cnx.cursor()
        cursor.execute(
        f"CREATE DATABASE {database} DEFAULT CHARACTER SET 'utf8'")
        run_code(tables.categories)
        run_code(tables.flash_cards)
        run_code(tables.projects)
        run_code(tables.questions)
        add_category('mysql')
        add_category('python')
        cnx.commit()
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    else:
        cursor.close()
        cnx.close()


def connect():
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database()
        else:
            print(err)
    else:
        cnx.close()
        
def run_code(code:str):
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor(f"USE {database}")
        cursor.execute(code)
        cnx.commit()
        print('Succeded')
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    else:
        cursor.close()
        cnx.close()
        
def add_category(category_name:list):
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor(f"USE {database}")
        add_cat = ("INSERT INTO categories "
               "(category) "
               "VALUES (%s)")
        cursor.execute(add_cat,[category_name])
        cnx.commit()
        print('Succeded')
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    else:
        cursor.close()
        cnx.close()
        
def add_data(data:dict):
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor(f"USE {database}")
        if data['category'].lower() == 'mysql':
            cat_id = 1
        elif data['category'].lower() == 'python':
            cat_id = 2
        else:
            add_category(data['category'])
            get_cat_id = """
                        SELECT category_id from categories
                        where category = %s
                                         """
            cursor.execute(get_cat_id,[data['category']])
            for (category_id) in cursor:
                cat_id = category_id
        cursor.execute(f"""
                        INSERT INTO flash_cards(category_id,answer,question)
                        VALUES ({cat_id}, '{data['answer']}', '{data['question']}')
                        """)
        cnx.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    finally:
        cursor.close()
        cnx.close()

