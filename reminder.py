import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from functools import partial
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from pygame import mixer
import time

class first(Widget):

   
    def alarm(self):
        Clock.schedule_interval(self.timer, 1)

    def timer(self, dt):
        n = str(time.localtime().tm_hour)
        m = str(time.localtime().tm_min)
        p = str(time.localtime().tm_sec)
        if n==self.hour.text and m==self.minutes.text and p==self.seconds.text:
            print("correct")
            
            sound = SoundLoader.load('C:/Users/DELL PC/Music/Am I Wrong - Nico & Vinz - 1400176550.mp3')
            sound.play()

            return False
            


class Reminder(App):
    def build(self):
        return first()


if __name__ == "__main__":
    Reminder().run()


