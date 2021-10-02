# from AutoBot import AutoBot, append_suffix, drop_suffix

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner

import os


class MyGridLayout(GridLayout):
    def spinner_clicked(self, value):
        print("Spinner Value " + value)
    pass

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()