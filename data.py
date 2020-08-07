import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
#from kivy.uix.button import Button

class data(Widget):
    name = ObjectProperty(None)
   
    def btn(self):
        name = "michael"
        self.name.text = self.name.text.lower()

        if name == self.name.text:
            return "Michael"
           

class DataApp(App):
    def build(self):
        return data()

if __name__ == "__main__" :
    DataApp().run()
