
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock


class Logo_page(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.go_to_screen ,5)
    
    def go_to_screen(self, sec):
        self.manager.current = "Page1"

class Page1(Screen): 
    count=0
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.update_label ,1)
    
    def update_label(self, num):
        self.count+=1
        self.ids.lbl_count.text=str(self.count)
    

class UI(ScreenManager):
    pass

class clockApp(App):
    def build(self):
        return UI()

if __name__ == "__main__":
    clockApp().run()
