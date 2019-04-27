import os

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


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
        with open(os.path.join(path, filename[0])) as stream:
            print(stream.read())
            #self.text_input.text = stream.read()

        self.dismiss_popup()

    def clicked_add(self):
        name = self.ids["text_name"].text
        wag = self.ids["text_wag"].text
        typ = self.ids["text_type"].text

        if name == "" or wag == "":
            return

        self.ids["text_wag"].text = ""

        try:
            wag = int(wag)
        except ValueError:
            print("ValueError")
            return

        self.ids["text_name"].text = ""

        print(name, wag)
        self.parent.send_info_to_stack([name, wag])

    def allsum(self):
        print("allsum")
