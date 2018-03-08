"""Provide the central game loop which drives everything"""
import os
import select
import time
import termios
import tty
from sys import stdin


import game_map as gm
import player as p
from display import display


class GameLoop:
    
    def game_loop(self):
        while True:
            os.system("clear")
            #            print(self.game_map.map)
            display(self.score, self.game_map.map, self.player)
            print(self.game_map.map)
            self.game_map.step()
            self.player.update(self.game_map)
            time.sleep(1.0)# + (player.speed * 0.05))
        """        fds = inpoll.poll(0)
        if fds != []:
            character = stdin.read(1)
            print("\r read this from stdin: " + character + "\n")
            stdin.flush()

            if character == 'q':
                break
        else:
            print("\r" + "No input this tick\n")
"""            


        

    def __init__(self):
        #    tty.setraw(stdin)
        self.game_map = gm.Map()
        self.player = p.Player(1, self.game_map.map[1])

        self.termattrs = termios.tcgetattr(stdin)
        self.inpoll = select.poll()
        self.inpoll.register(stdin, select.POLLIN)

        self.score = 0




gl = GameLoop()

gl.game_loop()



os.system("reset");
