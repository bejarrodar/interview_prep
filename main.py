from random import randint

from kivy.app import App  # @UnresolvedImport
from kivy.clock import mainthread  # @UnresolvedImport
from kivy.lang import Builder  # @UnresolvedImport
from kivy.properties import ObjectProperty, StringProperty  # @UnresolvedImport
from kivy.uix.boxlayout import BoxLayout  # @UnresolvedImport
from kivy.uix.button import Button  # @UnresolvedImport
from kivy.uix.screenmanager import Screen, ScreenManager  # @UnresolvedImport
from pygments.lexers.sql import MySqlLexer

import mysql_connector


class WindowManager(ScreenManager):
    def get_question(self,category):
        self.parent.get_question(category.text)
    pass

class NavBar(BoxLayout):
    pass

class StudyPage(Screen):
    button_list = []
    def set_cat_window(self,category):
        app.get_question(category.text)
        self.parent.current = 'flash_card'
    
    @mainthread
    def on_enter(self):
        self.button_list = []
        self.ids.buttons.clear_widgets()
        cat_list = mysql_connector.get_cat_list()
        for i in range(len(cat_list)):
            self.button_list.append(Button(text=cat_list[i]))
            self.button_list[i].bind(on_press= self.set_cat_window)
            self.ids.buttons.add_widget(self.button_list[i])

class FlashCard(Screen):
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

class CorrectFlash(Screen):
    button_list = []
    def set_cat_window(self,category):
        app.get_question(category.text)
        self.parent.current = 'flash_card'
    
    @mainthread
    def on_enter(self):
        self.button_list = []
        self.ids.buttons.clear_widgets()
        cat_list = mysql_connector.get_cat_list()
        for i in range(len(cat_list)):
            self.button_list.append(Button(text=cat_list[i]))
            self.button_list[i].bind(on_press= self.set_cat_window)
            self.ids.buttons.add_widget(self.button_list[i])

class WrongFlash(Screen):
    button_list = []
    def set_cat_window(self,category):
        app.get_question(category.text)
        self.parent.current = 'flash_card'
    
    @mainthread
    def on_enter(self):
        self.button_list = []
        self.ids.buttons.clear_widgets()
        cat_list = mysql_connector.get_cat_list()
        for i in range(len(cat_list)):
            self.button_list.append(Button(text=cat_list[i]))
            self.button_list[i].bind(on_press= self.set_cat_window)
            self.ids.buttons.add_widget(self.button_list[i])

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
    
    def get_question(self,category):
        data = mysql_connector.get_question(category)
        if data:
            self.question = data[0]
            self.correct = randint(1,4)
            match self.correct:
                case 1:
                    self.ans_a = data[1]
                    self.ans_b = data[2]
                    self.ans_c = data[3]
                    self.ans_d = data[4]
                case 2:
                    self.ans_a = data[2]
                    self.ans_b = data[1]
                    self.ans_c = data[3]
                    self.ans_d = data[4]
                case 3:
                    self.ans_a = data[3]
                    self.ans_b = data[2]
                    self.ans_c = data[1]
                    self.ans_d = data[4]
                case 4:
                    self.ans_a = data[4]
                    self.ans_b = data[2]
                    self.ans_c = data[3]
                    self.ans_d = data[1]

    def rem_wizard(self,answer,question,fake1,fake2,fake3):
        if answer.text != '':
            if question.text != '':
                mysql_connector.rem_flash(answer = answer.text,question = question.text)
            mysql_connector.rem_flash(answer = answer.text)
        else:
            mysql_connector.rem_flash(question = question.text)
        self.clear_rem_wizard(answer,question)
        if fake1.text != '' and fake2.text != '' and fake3.text != '':
            mysql_connector.clear_fake(fake1,fake2,fake3)
    
    def clear_rem_wizard(self,answer,question,fake1,fake2,fake3):
        answer.text = ''
        question.text = ''
        fake1.text = ''
        fake2.text = ''
        fake3.text = ''
    
    def add_wizard(self,category,answer,question,fake1,fake2,fake3):
        data = {'category':category.text,'answer':answer.text,'question':question.text,'fake1':fake1.text,'fake2':fake2.text,'fake3':fake3.text}
        if mysql_connector.add_data(data):
            self.clear_wizard(category,answer,question,fake1,fake2,fake3)


    def clear_wizard(self,category,answer,question,fake1,fake2,fake3):
        category.text = ''
        answer.text = ''
        question.text = ''
        fake1.text = ''
        fake2.text = ''
        fake3.text = ''
    
    def command_run(self,code):
        print(code)
        mysql_connector.run_code(code)
    
    def build(self):
        self.window = WindowManager()
        return self.window

if __name__ == '__main__':
    mysql_connector.connect()
    app = InterviewPrepApp()
    app.run()
