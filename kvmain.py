from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from kivy.config import Config
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
Config.set('input', 'mouse', 'mouse,disable_multitouch')
import os

from kivy.lang import Builder
from src.buttonzone import *
from src.cmdzone import *
from src.stackzone import *

kvfiles = [ 'ButtonZone.kv',
            'CmdZone.kv',
            'StackZone.kv',
            'denomination.kv',]

kv_path = 'kv'

for file in kvfiles:
    Builder.load_file(os.path.join(kv_path, file))


class RootWidget(BoxLayout):

    def __init__(self):
        super(RootWidget, self).__init__()
        Clock.schedule_once(self._after_kv_applied)

    def _after_kv_applied(self, dt):

        for zone in self.children:
            if zone.id_name == "stackzone":
                self.stackzone = zone
            elif zone.id_name == "buttonzone":
                self.buttonzone = zone
            elif zone.id_name == "cmdzone":
                self.cmdzone = zone

    def send_info_to_stack(self, workerinfo):
        print("in!")
        self.stackzone.add_workerinfo(workerinfo)
        print("out")

    def send_csvinfo_to_stack(self):
        pass

class TestApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    TestApp().run()
