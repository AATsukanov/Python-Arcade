import arcade
'''
Необхордимо установить старую версию питона python 3.9.13
https://www.python.org/downloads/release/python-3913/
потом создать с нуля проект и виртуальное окружение и в него установить arcade
'''
__author__ = 'Alexey A.Tsukanov'

#константы:
WIDTH = 800
HEIGHT = 600
TITLE = 'Multiscale Particles Ping-Pong (Python+arcade)'

class Bar(arcade.Sprite):

    def __init__(self):
        super().__init__(filename = 'multiscale-bar.png',
                         scale = 0.25)

    def update(self):
        self.center_x += self.change_x
        if self.right > WIDTH:
            self.right = WIDTH
        if self.left < 0:
            self.left = 0

class Ball(arcade.Sprite):

    def __init__(self):
        super().__init__(filename = 'multiscale-ball.png',
                         scale = 0.2)
        self.change_x = 2
        self.change_y = 2
        self.change_angle = 1

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.angle += self.change_angle

        if self.right > WIDTH:
            self.change_x *= -1
        if self.left < 0:
            self.change_x *= -1
        if self.top > HEIGHT:
            self.change_y *= -1
        if self.bottom < 0:
            self.change_y *= -1

class Game(arcade.Window):

    def __init__(self, width, height, title):
        self.bg = (255, 255, 255)
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        #рокетка:
        self.bar.center_x = WIDTH * 0.5
        self.bar.center_y = HEIGHT * 0.1
        #шар:
        self.ball.center_x = WIDTH * 0.5
        self.ball.center_y = HEIGHT * 0.5

    def on_draw(self):
        self.clear(self.bg)
        self.bar.draw()
        self.ball.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.change_y *= -1
            self.ball.change_angle *= -1
        self.ball.update()
        self.bar.update()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.bar.change_x = 3
        if symbol == arcade.key.LEFT:
            self.bar.change_x = -3

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
            self.bar.change_x = 0

def main():
    window = Game(WIDTH, HEIGHT, TITLE)
    arcade.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
