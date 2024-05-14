from kivy.uix.actionbar import ToggleButton
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class Scr1(Screen):
    pass

class Scr2(Screen): 
    def convert(self,*args):
        try:
            num = int(self.ids.txt_number.text)  
            if args[0].text=="base2":
                self.ids.lbl_output.text = bin(num)[2:]
            elif args[0].text=="base8":
                self.ids.lbl_output.text = oct(num)[2:]
            elif args[0].text=="base16": 
                self.ids.lbl_output.text = hex(num)[2:]   
        except ValueError:
            self.ids.lbl_output.text = "Invalid input!"

class UI(ScreenManager):
    pass

class ConvertApp(App):
    def build(self):
        return UI()

if __name__ == "__main__":
    ConvertApp().run()
