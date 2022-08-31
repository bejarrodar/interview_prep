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
        enter_initial_data()
        cnx.commit()
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    else:
        cursor.close()
        cnx.close()

def enter_initial_data():
    for each in knowledge:
        data = {'category':each[0],'question':each[1],'answer':each[2],'fake1':each[3],'fake2':each[4],'fake3':each[5]}
        add_data(data)
        
        

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
        
def add_category(category_name:str):
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
    flash_sql = """INSERT INTO flash_cards(category_id,question,answer,fakes_id) 
            VALUES(%s,%s,%s,%s)"""
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor()
        cat_id = get_category(data['category'])
        fakes_id = get_fakes(data['fake1'],data['fake2'],data['fake3'])
        cursor.execute(flash_sql,[cat_id, data['question'], data['answer'], fakes_id])
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
        cursor.execute("SELECT category_id FROM categories WHERE category = %s",[category])
        cat_id = cursor.fetchone()
        if cat_id:
            return cat_id[0]
        else:
            add_category(category)
            return get_category(category)
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

def get_fakes(fake1,fake2,fake3):
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor()
        cursor.execute("SELECT fakes_id FROM fakes WHERE fake1 IN (%s,%s,%s) AND fake2 IN (%s,%s,%s) AND fake3 IN (%s,%s,%s)",[fake1,fake2,fake3,fake1,fake2,fake3,fake1,fake2,fake3])
        fakes_id = cursor.fetchone()
        print(fakes_id)
        if fakes_id:
            return fakes_id[0]
        else:
            add_fakes(fake1,fake2,fake3)
            return get_fakes(fake1,fake2,fake3)
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    finally:
        cursor.close()
        cnx.close()

def add_fakes(fake1,fake2,fake3):
    fakes_sql = """INSERT INTO fakes(fake1,fake2,fake3) 
            VALUES(%s,%s,%s)"""
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor()
        cursor.execute(fakes_sql,[fake1,fake2,fake3])
        cnx.commit()
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    finally:
        cursor.close()
        cnx.close()
        
def clear_fake(fake1,fake2,fake3):
    fake_id = get_fakes(fake1,fake2,fake3)
    clear_fake_sql = "DELETE FROM fakes WHERE fakes_id = %s"
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor()
        cursor.execute(clear_fake_sql,[fake_id])
        cnx.commit()
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    finally:
        cursor.close()
        cnx.close()
        
def get_cat_list():
    try:
        cnx = mysql.connector.connect(user=login,password=password,host=host,database=database)
        cursor = cnx.cursor()
        cursor.execute("""SELECT DISTINCT category FROM categories""")
        categories = [x[0] for x in cursor]
        return categories
    except mysql.connector.Error as err:
        print(f"Failed executing code: {err}")
    finally:
        cursor.close()
        cnx.close()
