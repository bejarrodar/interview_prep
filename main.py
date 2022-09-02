from random import randint

from kivy.app import App  # @UnresolvedImport
from kivy.clock import mainthread  # @UnresolvedImport
from kivy.lang import Builder  # @UnresolvedImport
from kivy.properties import ObjectProperty, StringProperty  # @UnresolvedImport
from kivy.uix.boxlayout import BoxLayout  # @UnresolvedImport
from kivy.uix.button import Button  # @UnresolvedImport
from kivy.uix.gridlayout import GridLayout  # @UnresolvedImport
from kivy.uix.label import Label  # @UnresolvedImport
from kivy.uix.screenmanager import Screen, ScreenManager  # @UnresolvedImport
from kivy.uix.scrollview import ScrollView  # @UnresolvedImport
from pygments.lexers.sql import MySqlLexer

import mysql_connector


class WindowManager(ScreenManager):
    def get_question(self,category):
        self.parent.get_question(category.text)
    pass

class WrappedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)))
            #,texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

class WrappedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

class NavBar(BoxLayout):
    pass

class StudyPage(Screen):
    button_list = []
    def set_cat_window(self,category):
        app.get_question(category.text)
        self.parent.current = 'flash_card'
    
    @mainthread
    def on_enter(self):
        navbar = NavBar()
        self.add_widget(navbar)
        self.scroll_box = BoxLayout(size_hint=(.9,.9),pos_hint={'right':1,'top':.8})
        self.scroll = ScrollView()
        self.box = GridLayout(cols=2,size_hint_y= None,spacing=10)
        cat_list = mysql_connector.get_cat_list()
        self.add_widget(Label(text="What would you like to study?",size_hint=(1,.1),pos_hint={'top':1}))
        self.scroll = ScrollView(size_hint=(.9,1),pos_hint={'right':1})
        self.box = GridLayout(cols=2,size_hint_y= None,spacing=10)
        for i in range(len(cat_list)):
            this = Button(text=cat_list[i],size_hint_y=None,height='40dp')
            this.bind(on_press= self.set_cat_window)
            self.box.add_widget(this)
        self.scroll.add_widget(self.box)
        self.scroll_box.add_widget(self.scroll)
        self.add_widget(self.scroll_box)

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
        navbar = NavBar()
        self.add_widget(navbar)
        self.scroll_box = BoxLayout(size_hint=(.9,.9),pos_hint={'right':1,'top':.8})
        self.scroll = ScrollView()
        self.box = GridLayout(cols=2,size_hint_y= None,spacing=10)
        cat_list = mysql_connector.get_cat_list()
        self.add_widget(Label(text="",size_hint=(1,.1),pos_hint={'top':1}))
        self.scroll = ScrollView(size_hint=(.9,1),pos_hint={'right':1})
        self.box = GridLayout(cols=2,size_hint_y= None,spacing=10)
        for i in range(len(cat_list)):
            this = Button(text=cat_list[i],size_hint_y=None,height='40dp')
            this.bind(on_press= self.set_cat_window)
            self.box.add_widget(this)
        self.scroll.add_widget(self.box)
        self.scroll_box.add_widget(self.scroll)
        self.add_widget(self.scroll_box)

class WrongFlash(Screen):
    button_list = []
    def set_cat_window(self,category):
        app.get_question(category.text)
        self.parent.current = 'flash_card'
    
    @mainthread
    def on_enter(self):
        navbar = NavBar()
        self.add_widget(navbar)
        self.scroll_box = BoxLayout(size_hint=(.9,.9),pos_hint={'right':1,'top':.8})
        self.scroll = ScrollView()
        self.box = GridLayout(cols=2,size_hint_y= None,spacing=10)
        cat_list = mysql_connector.get_cat_list()
        self.add_widget(Label(text="",size_hint=(1,.1),pos_hint={'top':1}))
        self.scroll = ScrollView(size_hint=(.9,1),pos_hint={'right':1})
        self.box = GridLayout(cols=2,size_hint_y= None,spacing=10)
        for i in range(len(cat_list)):
            this = Button(text=cat_list[i],size_hint_y=None,height='40dp')
            this.bind(on_press= self.set_cat_window)
            self.box.add_widget(this)
        self.scroll.add_widget(self.box)
        self.scroll_box.add_widget(self.scroll)
        self.add_widget(self.scroll_box)

class ReviewProjects(Screen):
    def select_button(self,btn):
        self.box.clear_widgets()
        grid = GridLayout(cols=2,size_hint=(.9,1),pos_hint={'right':1},spacing=(.1,.1))
        project = mysql_connector.get_project(btn.text) #name,challenges,mistakes,enjoyed,leadership,conflicts,changes
        grid.add_widget(Label(text='Name:',size_hint=(.5,1)))
        grid.add_widget(Label(text=project[0][0]))
        grid.add_widget(Label(text='Challenges:',size_hint=(.5,1)))
        grid.add_widget(WrappedLabel(text=project[0][1]))
        grid.add_widget(Label(text='Mistakes:',size_hint=(.5,1)))
        grid.add_widget(WrappedLabel(text=project[0][2]))
        grid.add_widget(Label(text='Enjoyed:',size_hint=(.5,1)))
        grid.add_widget(WrappedLabel(text=project[0][3]))
        grid.add_widget(Label(text='Leadership:',size_hint=(.5,1)))
        grid.add_widget(WrappedLabel(text=project[0][4]))
        grid.add_widget(Label(text='Conflicts:',size_hint=(.5,1)))
        grid.add_widget(WrappedLabel(text=project[0][5]))
        grid.add_widget(Label(text='What You Would Do Different:',size_hint=(.5,1)))
        grid.add_widget(WrappedLabel(text=project[0][6]))
        self.add_widget(grid)
    
    @mainthread
    def on_enter(self):
        navbar = NavBar()
        self.add_widget(navbar)
        project_names = mysql_connector.get_project_names()
        self.scroll = ScrollView(size_hint=(.9,1),pos_hint={'right':1})
        self.box = GridLayout(cols=2,size_hint_y= None,spacing=10)
        for each in project_names:
            this_button = Button(text=each[0],size_hint_y=None,height='40dp')
            this_button.bind(on_press= self.select_button)
            self.box.add_widget(this_button)
        self.scroll.add_widget(self.box)
        self.add_widget(self.scroll)

class ReviewQA(Screen):
    def select_button(self,btn):
        self.box.clear_widgets()
        grid = GridLayout(cols=2,size_hint=(.9,1),pos_hint={'right':1},spacing=(.1,.1))
        project = mysql_connector.get_qa(btn.text) #name,challenges,mistakes,enjoyed,leadership,conflicts,changes
        grid.add_widget(Label(text='Question:',size_hint=(.5,1)))
        grid.add_widget(WrappedLabel(text=project[0][0]))
        grid.add_widget(Label(text='Answer:',size_hint=(.5,1)))
        grid.add_widget(WrappedLabel(text=project[0][1]))
        self.add_widget(grid)
    
    @mainthread
    def on_enter(self):
        navbar = NavBar()
        self.add_widget(navbar)
        questions = mysql_connector.get_questions()
        self.scroll = ScrollView(size_hint=(.9,1),pos_hint={'right':1})
        self.box = GridLayout(cols=2,size_hint_y= None,spacing=10)
        for each in questions:
            this_button = WrappedButton(text=each[0],size_hint_y=None,height='40dp')
            this_button.bind(on_press= self.select_button)
            self.box.add_widget(this_button)
        self.scroll.add_widget(self.box)
        self.add_widget(self.scroll)

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
        
    def add_qa(self,question,answer):
        mysql_connector.add_qa(question.text,answer.text)
        question.text = ''
        answer.text = ''
        
    def add_project(self,project_name,challenges,mistakes,enjoyed,leadership,conflicts,different):
        mysql_connector.add_project(project_name.text,challenges.text,mistakes.text,enjoyed.text,leadership.text,conflicts.text,different.text)
        project_name.text = ''
        challenges.text = ''
        mistakes.text = ''
        enjoyed.text = ''
        leadership.text = ''
        conflicts.text = ''
        different.text = ''
    
    def build(self):
        self.window = WindowManager()
        return self.window

if __name__ == '__main__':
    mysql_connector.connect()
    app = InterviewPrepApp()
    app.run()
