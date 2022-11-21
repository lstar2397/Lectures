import sys
from sense_hat import SenseHat

sense = SenseHat()

class Player:
    def __init__(self):
        self.x = 1
        self.y = 6
        self.set_hp(8)
        self.attacks = []

    def set_hp(self, hp):
        if hp > 0:
            self.hp = hp
            self.show_hp()
        else:
            self.gameover()

    def show_hp(self):
        for i in range(self.hp):
            sense.set_pixel(i, 7, 0, 255, 0)

    def move(self, direction):
        x = self.x
        y = self.y
        
        self.show_pos((0, 0, 0))

        if direction == "left" and x >= 1:
            x -= 1
            """
        elif direction == "up" and y >= 1:
            y -= 1
            """
        elif direction == "right" and x <= 6:
            x += 1
            """
        elif direction == "down" and y <= 6:
            y += 1
            """

        self.show_pos((0, 0, 255))
        
        self.x = x
        self.y = y

    def show_pos(self, color):
        x = self.x
        y = self.y
        
        sense.set_pixel(x, y - 1, color)
        sense.set_pixel(x - 1, y, color)
        sense.set_pixel(x, y, color)
        sense.set_pixel(x + 1, y, color)

    def attack(self):
        for i in range(5):
            if i != 0:
                sense.set_pixel(self.x, self.y - 1 - i, 0, 0, 0)
            sense.set_pixel(self.x, self.y - 2 - i, 255, 0, 0)
        self.attacks.append(self.x)

    def gameover():
        sense.show_message("Game Over!", text_colour=[255, 255, 0])
        sense.clear()
        sys.exit()
