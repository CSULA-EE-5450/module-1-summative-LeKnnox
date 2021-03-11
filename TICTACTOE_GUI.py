from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)


class TicTacToeGame(Widget):

    player1 = ObjectProperty(None)

    def on_touch_up(self, touch):
        if touch.x < (self.center_x - (self.center_x / 3)):
            if touch.x < (self.center_y + (self.center_y / 3)):
                self.player1.score += 1
                #self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

    pass


class TicTacToeApp(App):
    def build(self):
        game = TicTacToeGame()
        #game.serve_ball()
        #Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    TicTacToeApp().run()