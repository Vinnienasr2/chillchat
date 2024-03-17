from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from classes import RegistrationScreen


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"  # You can change it to "Light"
        return Builder.load_file("main.kv")

    def on_registration_button_press(self, country_code, mobile_number):
        # Add your registration logic here
        print("Country Code:", country_code)
        print("Mobile Number:", mobile_number)


if __name__ == "__main__":
    MyApp().run()
