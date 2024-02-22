from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineAvatarIconListItem, MDList
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager


class VerificationScreen(Screen):
    pass

class RegistrationScreen(Screen):
    pass

class NavBar(CommonElevationBehavior, MDFloatLayout):
    pass

class ChatListScreen(Screen):
    pass

class GroupScreen(Screen):
    pass

class UpdatesScreen(Screen):
    pass

class CallScreen(Screen):
    pass

class MimoScreen(Screen):
    pass

class MainApplication(Screen):
    pass

class MessageScreen(Screen):
    Builder.load_file('message.kv')
    screen_manager = ScreenManager()

class MessageItem(OneLineAvatarIconListItem):
    pass