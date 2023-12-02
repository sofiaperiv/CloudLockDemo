from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import Screen
from kivy.graphics import Color, Ellipse
from kivymd.uix.card import MDCard
from kivy.graphics import Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    def ask_permission(self):
        ask_permission = self.ids.ask_permission
        permission = self.ids.permission
        # self.ids.permission.text = "Доступ одержано!"
        # self.ids.ask_permission.source = 'images/Open_Button.png'

        if permission.text == 'Ви не маєте доступу до цього приміщення.':
            permission.text = 'Доступ до псєчої буди надано. Ви можете відкрити її'
            permission.color = 46 / 255, 204 / 255, 113 / 255, 1
        elif permission.text == 'Доступ до псєчої буди надано. Ви можете відкрити її':
            permission.text = 'Зараз псєча буда відкрита'
            permission.color = "gray"
        elif permission.text == 'Зараз псєча буда відкрита':
            permission.text = 'Доступ до псєчої буди надано. Ви можете відкрити її'
            permission.color = 46 / 255, 204 / 255, 113 / 255, 1

        if ask_permission.source == 'images/Ask_Button.png':
            ask_permission.source = 'images/Open_Button.png'
        elif ask_permission.source == 'images/Open_Button.png':
            ask_permission.source = 'images/Close_Door.png'
        elif ask_permission.source == 'images/Close_Door.png':
            ask_permission.source = 'images/Open_Button.png'


class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class MyRectangle(MDFloatLayout):
    pass


class HomeScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass





class MyApp(MDApp):

    def build(self):
        kv = Builder.load_file("mainScreen.kv")
        return kv

    def change_color(self, instance):
        if instance in self.root.ids.values():
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            for i in range(3):
                if f"nav_icon{i + 1}" == current_id:
                    self.root.ids[f"nav_icon{i + 1}"].text_color = 1, 0, 0, 1
                else:
                    self.root.ids[f"nav_icon{i + 1}"].text_color = 0, 0, 0, 1



if __name__ == "__main__":
    MyApp().run()
