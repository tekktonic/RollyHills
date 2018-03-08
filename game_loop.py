"""Provide the central game loop which drives everything"""
import os
import select
import time
import timeit
import termios
import tty
from sys import stdin


import game_map as gm
import player as p
from display import display


class GameLoop:
    """Provide the main game loop"""
    def game_loop(self):
        """The actual game loop itself"""
        while True:
            os.system("clear")
            #            print(self.game_map.map)
            display(self.score, self.game_map.map, self.player)
            self.game_map.step()
            self.player.update(self.game_map)
            tty.setraw(stdin)
            start_time = time.perf_counter()
            fds = self.inpoll.poll(500)
            poll_time = time.perf_counter() - start_time

            sleep_time = max(0, (0.2 - (self.speed * 0.05)) - poll_time)
            print(fds)
            if fds != []:
                character = stdin.read(1)
                stdin.flush()

                if character == 'q':
                    break
                elif character == 'f':
                    self.speed += 5
                    self.player.x += 1
                elif character == 'b':
                    self.speed -= 5
                    self.player.x -= 1
                elif character == 'j':
#                    print("J PRESSED GUYS PLEASE NOTICE ME")
                    self.player.jump()
            
                time.sleep(sleep_time)
        termios.tcsetattr(stdin, termios.TCSANOW, self.termattrs)

                    

    def reset(self):
        """Re-perform initialization and then play again"""
        self.__init__(self)
        self.game_loop()

    def __init__(self):
        """ Initialize game state for a new game"""
        #    tty.setraw(stdin)
        self.game_map = gm.Map()
        self.player = p.Player(8, self.game_map.map[8])
        self.speed = 0
        self.termattrs = termios.tcgetattr(stdin)
        self.inpoll = select.poll()
        self.inpoll.register(stdin, select.POLLIN)

        self.score = 0




GAME = GameLoop()

GAME.game_loop()



os.system("reset")
