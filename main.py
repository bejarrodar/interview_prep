from unicodedata import category

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from pygments.lexers.sql import MySqlLexer

import mysql_connector


class WindowManager(ScreenManager):
    pass

class NavBar(BoxLayout):
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

kv = Builder.load_file('main.kv')

class InterviewPrepApp(App):
    lexer = ObjectProperty(MySqlLexer())
    
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
        WindowManager().add_widget(StudyPage())
        return WindowManager()

if __name__ == '__main__':
    mysql_connector.connect()
    InterviewPrepApp().run()
