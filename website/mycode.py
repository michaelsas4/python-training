import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout ()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="school: "))
        self.school = TextInput(multiline=False)
        self.inside.add_widget(self.school)

        self.inside.add_widget(Label(text="username: "))
        self.username = TextInput(multiline=False)
        self.inside.add_widget(self.username)

        self.inside.add_widget(Label(text="password: "))
        self.password = TextInput(multiline=False)
        self.inside.add_widget(self.password)

        self.inside.add_widget(Label(text="age: "))
        self.age = TextInput(multiline=False)
        self.inside.add_widget(self.age)

        self.inside.add_widget(Label(text="Country: "))
        self.country = TextInput(multiline=False)
        self.inside.add_widget(self.country)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        school = self.school.text
        username = self.username.text
        password = self.password.text
        age = self.age.text
        country = self.country.text

        print("name:", name, "Last Name:", last, "school:", school, "username:", username, "password:", password, "age:", age, "country:", country)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
