import os

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

from kivy.properties import ObjectProperty, StringProperty, NumericProperty

class StackZone(BoxLayout):
    workerinfos = []
    id_name = "stackzone"

    def add_workerinfo(self, workerinfo):

        WI = WorkerInfo(workerinfo)
        self.workerinfos.append(WI)
        self.ids["stacknamelabel"].text += WI.name + "\n"
        self.ids["stackwaglabel"].text += str(WI.wag) + "\n"

        print(self.workerinfos)

    def clean_workerinfo(self):
        self.workerinfos = []
        self.clean_widget()

class WorkerInfo(BoxLayout):
    name = ""
    wag = 0

    def __init__(self, workerinfo, **kwargs):
        self.name = workerinfo[0]
        if len(self.name) >= 10:
            self.name = self.name[:10]
        self.wag = workerinfo[1]
