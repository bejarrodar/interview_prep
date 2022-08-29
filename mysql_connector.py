login = "root"
password = "root"
database = "interviewprep"
host='127.0.0.1'


from random import randint

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

def rem_flash(answer = None,question = None):
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor(f"USE {database}")
        if answer:
            if question:
                cursor.execute(f"""
                               DELETE FROM flash_cards WHERE answer = '{answer}' AND question = '{question}'
                               """)
            cursor.execute(f"""
                               DELETE FROM flash_cards WHERE answer = '{answer}'
                               """)
        else:
            cursor.execute(f"""
                               DELETE FROM flash_cards WHERE question = '{question}'
                               """)
        cnx.commit()
        print('Succeded')
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    else:
        cursor.close()
        cnx.close()

def get_question(category):
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor(f"USE {database}")
        qa = []
        if category.lower() == 'mysql':
            cat_id = 1
            cursor.execute("SELECT COUNT(flash_id) as count FROM flash_cards WHERE category_id = 1")
            for (count) in cursor:
                if count[0] > 4:
                    limit_num = randint(0,count-4)
                else:
                    return None
        if category.lower() == 'python':
            cat_id = 2
            cursor.execute("SELECT COUNT(flash_id) as count FROM flash_cards WHERE category_id = 2")
            for (count) in cursor:
                print(count[0])
                if count[0] > 4:
                    limit_num = randint(0,count[0]-4)
                else:
                    return None
        else:
            return None
        cursor.execute(f"SELECT answer, question FROM flash_cards WHERE category_id = {cat_id} LIMIT {limit_num},4")
        for (answer,question) in cursor:
            qa.append([answer,question])
        print('Succeded')
        return qa
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    finally:
        cursor.close()
        cnx.close()
