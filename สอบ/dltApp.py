from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import StringProperty

# ตั้งค่าฟอนต์ภาษาไทย (ต้องตรวจสอบว่า tahoma.ttf ถูกติดตั้งในระบบหรือไม่)
Builder.load_string("""
<CustomPopup>:
    title: ""
    size_hint: None, None
    size: 400, 200
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: root.message
            font_name: 'tahoma.ttf'  # ตั้งค่าฟอนต์ภาษาไทย (ต้องตรวจสอบว่าถูกติดตั้งในระบบหรือไม่)
            font_size: 18
            halign: 'center'
        Button:
            text: 'OK'
            size_hint_y: 0.3
            on_press: root.dismiss()
""")

class CustomPopup(Popup):
    message = StringProperty("")

class Scr_home(Screen):
    pass

class Scr_register(Screen):
    
    def show_popup(self, title, message):
        popup = CustomPopup(title=title, message=message)
        popup.open()

    def validate_inputs(self):
        txt_cardcode = self.ids.txt_cardcode
        txt_ccode = self.ids.txt_ccode
        txt_tel = self.ids.txt_tel
        txt_email = self.ids.txt_email

        if not txt_cardcode.text.strip() or len(txt_cardcode.text) != 13:
            self.show_popup("ข้อมูลไม่ถูกต้อง", "กรุณากรอกเลขบัตรประชาชนให้มี 13 ตัวอักษร")
            return False

        if not txt_ccode.text.strip() or len(txt_ccode.text) != 13 or txt_ccode.text != txt_cardcode.text:
            self.show_popup("ข้อมูลไม่ถูกต้อง", "กรุณากรอกเลขบัตรประชาชนให้ตรงกันทั้งสองช่อง")
            return False

        if not txt_tel.text.strip() or len(txt_tel.text) != 10:
            self.show_popup("ข้อมูลไม่ถูกต้อง", "กรุณากรอกเบอร์โทรศัพท์ให้ถูกต้อง (10 ตัวอักษร)")
            return False

        if not txt_email.text.strip():
            self.show_popup("ข้อมูลไม่ครบ", "กรุณากรอกอีเมล")
            return False

        return True

    def process_registration(self):
        if self.validate_inputs():
            self.show_popup("บันทึกข้อมูล", "ทำการบันทึกข้อมูลเรียบร้อยแล้ว")
            # ทำการดำเนินการบันทึกข้อมูลต่อไปที่นี่

class Ui(ScreenManager):
    pass

class dltApp(App):
    def build(self):
        return Ui()

if __name__ == "__main__":
    dltApp().run()
