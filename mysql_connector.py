from random import randint

import mysql.connector
from mysql.connector import errorcode

import tables
from config import database, host, login, password
from starting_knowledge import knowledge


def create_database():
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host)
        cursor = cnx.cursor()
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
        run_code(tables.categories)
        run_code(tables.fakes)
        run_code(tables.flash_cards)
        run_code(tables.projects)
        run_code(tables.questions)
        add_category('mysql')
        add_category('python')
        enter_initial_data()
        cnx.commit()
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    else:
        cursor.close()
        cnx.close()

def enter_initial_data():
    for each in knowledge:
        run_code(each)

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
        cursor = cnx.cursor()
        cursor.execute("{}".format(code))
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
        cursor = cnx.cursor()
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
        cursor = cnx.cursor()
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
        cursor.execute("""
                        INSERT INTO flash_cards(category_id,answer,question)
                        VALUES (%s, %s, %s)
                        """,[cat_id, data['answer'], data['question']])
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
        cursor = cnx.cursor()
        if answer:
            if question:
                cursor.execute("""
                               DELETE FROM flash_cards WHERE answer = %s AND question = %s
                               """,[answer,question])
            cursor.execute("""
                               DELETE FROM flash_cards WHERE answer = %s
                               """,[answer])
        else:
            cursor.execute("""
                               DELETE FROM flash_cards WHERE question = %s
                               """,[question])
        cnx.commit()
        print('Succeded')
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    else:
        cursor.close()
        cnx.close()
        
def get_category(category):
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor()
        if category == 'mysql': cat_id = 1
        elif category == 'python': cat_id = 2
        else:
            cursor.execute("SELECT category_id FROM categories WHERE category = %s",[category])
            cat_id = cursor.fetchone()
        return cat_id
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    finally:
        cursor.close()
        cnx.close()

def get_question(category):
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor()
        cat_id = get_category(category)
        cursor.execute("SELECT count(flash_id) FROM flash_cards WHERE category_id = %s",[cat_id])
        questionslen = cursor.fetchone()[0]
        question_num = randint(1,questionslen)
        cursor.execute("SELECT * FROM flash_cards WHERE category_id = %s LIMIT %s,1",[cat_id,question_num-1])
        question = cursor.fetchone()
        cursor.execute("SELECT * FROM fakes WHERE fakes_id = %s",[question[4]])
        fakes = cursor.fetchone()
        return [question[3],question[2],fakes[1],fakes[2],fakes[3]]
        
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    finally:
        cursor.close()
        cnx.close()
