import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline=False)
        self.add_widget(self.lastname)

        self.add_widget(Label(text="School: "))
        self.school = TextInput(multiline=False)
        self.add_widget(self.school)

        self.add_widget(Label(text="username: "))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="password: "))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label(text="age: "))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)

        self.add_widget(Label(text="Country: "))
        self.Country = TextInput(multiline=False)
        self.add_widget(self.Country)

        
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()





