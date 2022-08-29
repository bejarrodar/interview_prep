from random import randint

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from pygments.lexers.sql import MySqlLexer

import mysql_connector


class WindowManager(ScreenManager):
    pass

class NavBar(BoxLayout):
    pass

class CategoryButtons(BoxLayout):
    pass

class StudyPage(Screen):
    pass

class Projects(Screen):
    pass

class DataManager(Screen):
    pass

class QA(Screen):
    pass

class Commands(Screen):
    pass

class Add_Wizard(Screen):
    pass

class Rem_Wizard(Screen):
    pass

class StudyMysql(Screen):
    pass

class StudyPython(Screen):
    pass

class CorrectFlash(Screen):
    pass

class WrongFlash(Screen):
    pass

kv = Builder.load_file('main.kv')

class InterviewPrepApp(App):
    lexer = ObjectProperty(MySqlLexer())
    question = StringProperty('')
    ans_a = StringProperty('')
    ans_b = StringProperty('')
    ans_c = StringProperty('')
    ans_d = StringProperty('')
    correct = 0
    
    def check_answer(self,button):
        self.question = ''
        self.ans_a = ''
        self.ans_b = ''
        self.ans_c = ''
        self.ans_d = ''
        if button == self.correct:
            self.window.current = 'correct_flash'
        else:
            self.window.current = 'wrong_flash'
    
    def get_mysql_question(self):
        data = mysql_connector.get_question('mysql')
        if data:
            self.question = data[0][1]
            self.correct = randint(1,4)
            match self.correct:
                case 1:
                    self.ans_a = data[0][0]
                    self.ans_b = data[1][0]
                    self.ans_c = data[2][0]
                    self.ans_d = data[3][0]
                case 2:
                    self.ans_a = data[1][0]
                    self.ans_b = data[0][0]
                    self.ans_c = data[2][0]
                    self.ans_d = data[3][0]
                case 3:
                    self.ans_a = data[2][0]
                    self.ans_b = data[1][0]
                    self.ans_c = data[0][0]
                    self.ans_d = data[3][0]
                case 4:
                    self.ans_a = data[3][0]
                    self.ans_b = data[1][0]
                    self.ans_c = data[2][0]
                    self.ans_d = data[0][0]
        
    def get_python_question(self):
        data = mysql_connector.get_question('python')
        if data:
            self.question = data[0][1]
            self.correct = randint(1,4)
            match self.correct:
                case 1:
                    self.ans_a = data[0][0]
                    self.ans_b = data[1][0]
                    self.ans_c = data[2][0]
                    self.ans_d = data[3][0]
                case 2:
                    self.ans_a = data[1][0]
                    self.ans_b = data[0][0]
                    self.ans_c = data[2][0]
                    self.ans_d = data[3][0]
                case 3:
                    self.ans_a = data[2][0]
                    self.ans_b = data[1][0]
                    self.ans_c = data[0][0]
                    self.ans_d = data[3][0]
                case 4:
                    self.ans_a = data[3][0]
                    self.ans_b = data[1][0]
                    self.ans_c = data[2][0]
                    self.ans_d = data[0][0]
    
    def rem_wizard(self,answer,question):
        if answer.text != '':
            if question.text != '':
                mysql_connector.rem_flash(answer = answer.text,question = question.text)
            mysql_connector.rem_flash(answer = answer.text)
        else:
            mysql_connector.rem_flash(question = question.text)
        self.clear_rem_wizard(answer,question)
    
    def clear_rem_wizard(self,answer,question):
        answer.text = ''
        question.text = ''
    
    def add_wizard(self,mysql,python,answer,question):
        if mysql.active:
            cat = 'mysql'
        if python.active:
            cat = 'python'
        data = {'category':cat,'answer':answer.text,'question':question.text}
        if mysql_connector.add_data(data):
            self.clear_wizard(mysql,python,answer,question)


    def clear_wizard(self,mysql,python,answer,question):
        mysql.active = False
        python.active = False
        answer.text = ''
        question.text = ''
    
    def command_run(self,code):
        print(code)
        mysql_connector.run_code(code)
    
    def build(self):
        self.window = WindowManager()
        return self.window

if __name__ == '__main__':
    mysql_connector.connect()
    InterviewPrepApp().run()
