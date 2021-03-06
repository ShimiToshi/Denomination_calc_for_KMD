import os

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import csv


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    current_dir = os.path.dirname(os.path.abspath(__file__))

class ButtonZone(BoxLayout):
    id_name = "buttonzone"

    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load File", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        workerinfos = []
        with open(os.path.join(path, filename[0]), "r") as f:
            reader = csv.reader(f)
            header = next(reader)

            for data in reader:
                if data[2] == "JPY":
                    data[1] = int(data[1])
                else:
                    data[1] = float(data[1])
                workerinfos.append(data)

        self.parent.send_csvinfo_to_stack(workerinfos)
        self.dismiss_popup()

    def clicked_add(self):
        name = self.ids["text_name"].text
        wag = self.ids["text_wag"].text
        typ = self.ids["text_type"].text

        if name == "" or wag == "":
            return

        self.ids["text_wag"].text = ""

        if typ == "JPY":
            try:
                wag = int(wag)
            except ValueError:
                print("ValueError")
                return
        else:
            wag = float(wag)

        self.ids["text_name"].text = ""

        print(name, wag)
        self.parent.send_info_to_stack([name, wag, typ])

    def allsum(self):
        print("allsum")
        self.parent.send_info_to_cmd()

    def resetcmd(self):
        self.parent.reset_cmd()
