import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget


class KivPongGame(Widget):
    pass


class KivPongApp(App):
    def build(self):
        return KivPongGame()


if __name__ == '__main__':
    KivPongApp().run()
