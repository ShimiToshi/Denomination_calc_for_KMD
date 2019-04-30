
import os

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.clock import Clock

class CmdZone(BoxLayout):
    id_name = "cmdzone"

    stack = []
    _inittxt = "[color=00d123]"

    def __init__(self, **kwargs):
        super(CmdZone, self).__init__(**kwargs)
        Clock.schedule_once(self._after_kv_applied)

    def _after_kv_applied(self, dt):
        self.cmdarea = self.ids["cmdarea"]
        self.reset_area()

    def reset_area(self):
        self.cmdarea.text = self._inittxt

    def get_stacks(self, stack):
        self.stack = stack
        self.stack.reverse()
        self.event = Clock.schedule_interval(self.check_stack, 0.2)
        print("start!", stack)

    def check_stack(self, dt):
        if self.stack:
            workerinfo = self.stack.pop()
            txt = "[size=20][color=cc6666]NAME : {: >10}[/color],   [color=22aa33]WAGS : {: ^10}[/color],   [color=4477cc]TYPE: {: ^5}[/color][/size]".format(workerinfo.name, workerinfo.wag, workerinfo.typ)
            self.cmdarea.text += txt +"\n"
            self.cmdarea.text += self.denomination_txt(*workerinfo.run()) +"\n"

        else:
            self.event.cancel()

    def denomination_txt(self, datas, opeinfo):
        txt = ""

        flag = False
        for data in datas:
            if data[0] >= 1:
                txt += money_format(data, opeinfo["main"]) + ",  "
            else:
                if not flag:
                    txt += "\n"
                    flag = True
                data[0] = int(data[0] * opeinfo["subrate"])
                txt += money_format(data, opeinfo["sub"]) + ",  "
        txt += "\n\n"

        return txt


def money_format(data, ope):
    return "[color=eeeeee]{: >3}[/color][color=cccccc]{: ^3}[/color] [{:^1}]".format(str(data[0]), ope, data[1])
