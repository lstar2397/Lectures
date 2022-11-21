import socket
import threading
from player import Player
from sense_hat import SenseHat
from time import sleep

HOST = '192.168.0.2'
PORT = 1919
ADDR = (HOST, PORT)
BUFSIZE = 1024

sense = SenseHat()
sense.clear()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)

player = Player()

def pushed_left(event):
    if event.action == "pressed":
        player.move("left")
        
def pushed_right(event):
    if event.action == "pressed":
        player.move("right")

def pushed_middle(event):
    player.attack()

def getEnemyAttack():
    while True:
        data = sock.recv(1024)
        if not data:
            pass
        else:
            x = 7 - int(data)
            for i in range(5):
                if i != 0:
                    sense.set_pixel(x, i - 1, 0, 0, 0)
                sense.set_pixel(x, i, 255, 0, 0)
            if x == self.x:
                player.set_hp(self.hp - 1)
    sock.close()

def sendAttack():
    while True:
        for attack in range(len(player.attacks)):
            data = x.pop(0).encode("UTF-8")
            sock.send(data)
    sock.close()

threading._start_new_thread(getEnemyAttack, ())
threading._start_new_thread(sendAttack, ())
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program ended")