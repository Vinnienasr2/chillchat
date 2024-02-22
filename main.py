from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.widget import Widget
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.core.window import Window
import sys
from kivy.uix.gridlayout import GridLayout
import kivy.resources
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout, MDNavigationDrawerMenu, MDNavigationDrawerHeader, MDNavigationDrawerLabel, MDNavigationDrawerDivider, MDNavigationDrawerItem
from kivymd.uix.bottomnavigation import MDBottomNavigation
from classes import RegistrationScreen, VerificationScreen, MainApplication, MessageItem, MessageScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp


Window.size = (370, 800)


class ChillChatApp(MDApp):
    def build(self):
        Builder.load_file('main.kv')
        screen_manager = ScreenManager()
        screen_manager.add_widget(RegistrationScreen(name='registration'))
        screen_manager.add_widget(VerificationScreen(name='verification'))
        screen_manager.add_widget(MainApplication(name='main'))
        screen_manager.add_widget(MessageScreen(name='message'))
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return screen_manager
    
    def register_user(self):
        phone_number = self.root.get_screen('registration').ids.phone_number.text
        if getattr(sys, 'frozen', False):
            kivy.resources.resource_add_path(sys._MEIPASS)
        self.root.current = 'verification'
        
    def verify_code(self):
        digit1 = self.root.get_screen('verification').ids.digit1.text
        digit2 = self.root.get_screen('verification').ids.digit2.text
        digit3 = self.root.get_screen('verification').ids.digit3.text
        digit4 = self.root.get_screen('verification').ids.digit4.text
        digit5 = self.root.get_screen('verification').ids.digit5.text
        digit6 = self.root.get_screen('verification').ids.digit6.text
        
        verification_code = digit1 + digit2 + digit3 + digit4 + digit5 + digit6
        print(f"Verification code: {verification_code}")
        self.root.current = 'main'

    def focus_next(self, current_field, next_field_id):
        current_field.focus = False
        self.root.get_screen('verification').ids[next_field_id].focus = True
        
        
    def on_start(self):
        # Populate the chat list with TwoLineAvatarListItem
        chat_list = self.root.get_screen('main').ids.chat_list
        for i in range(1, 4):
            item = TwoLineAvatarListItem(text=f'Chat {i} title', secondary_text=f'Chat {i} description')
            avatar = ImageLeftWidget(source=f'path_to_avatar_image_{i}.png')
            item.add_widget(avatar)
            item.bind(on_press=lambda x, chat_num=i: self.open_message_screen(chat_num))
            chat_list.add_widget(item)
            
    def open_message_screen(self, chat_num):
    # Switch to the message screen for the selected chat
        self.root.current = 'message'
        
    def back_to_chat_list(self):
        # Switch back to the chat list screen from the message screen
        self.root.current = 'main'
        
    def send_message(self):
        # Get the message from the input field
        message = self.root.get_screen('message').ids.message_input.text

        # Create a card with the message and add it to the messages area
        card = MDCard(
            size_hint=(None, None), 
            size=(dp(150), dp(50)), 
            pos_hint={'center_x': 0.75}, 
            md_bg_color=(0.7, 0.7, 0.7, 1),
            orientation="vertical",
            padding=(dp(8), dp(8), dp(8), dp(8)),  # Add padding (left, top, right, bottom)
            radius=[dp(10), dp(10), dp(10), dp(10)],  # Add rounded corners
            elevation=1,)
        
        
        label = MDLabel(text=message, theme_text_color="Custom", text_color=(0, 0, 0, 1))

        card.add_widget(label)

        messages_area = self.root.get_screen('message').ids.messages_area
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        messages_layout = BoxLayout(orientation='vertical', spacing=dp(10))  # Add spacing between cards
        messages_layout.add_widget(card)
        scroll_view.add_widget(messages_layout)
        messages_area.add_widget(scroll_view)
        
        scroll_view.height = messages_layout.height

        if message:
            self.root.get_screen('message').ids.message_input.text = ""

if __name__ == '__main__':
    ChillChatApp().run()