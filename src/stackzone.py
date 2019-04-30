import os

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

from kivy.properties import ObjectProperty, StringProperty, NumericProperty

from .denomination_calc import all_coin_calc

class StackZone(BoxLayout):
    workerinfos = []
    id_name = "stackzone"

    def add_workerinfo(self, workerinfo):

        WI = WorkerInfo(workerinfo)
        self.workerinfos.append(WI)
        self.ids["stacknamelabel"].text += WI.name + "\n"
        self.ids["stackwaglabel"].text += str(WI.wag) + "\n"
        self.ids["stacktypelabel"].text += WI.typ + "\n"

        print(self.workerinfos)

    def clean_workerinfo(self):
        self.workerinfos = []
        self.ids["stacknamelabel"].text = ""
        self.ids["stackwaglabel"].text = ""
        self.ids["stacktypelabel"].text = ""

    def load_stacks(self):
        stack = self.workerinfos
        self.clean_workerinfo()
        return stack

class WorkerInfo(BoxLayout):
    name = ""
    wag = 0
    typ = "JPY"

    def __init__(self, workerinfo, **kwargs):
        self.name = workerinfo[0]
        if len(self.name) >= 9:
            self.name = self.name[:9]
        self.wag = workerinfo[1]
        self.typ = workerinfo[2]

    def run(self):
        rets, opeinfo = all_coin_calc(self.wag, self.typ)
        return rets, opeinfo
