import variables
import game_map
import sys

class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dy = 0


    def update(self, game_map):
        self.y += self.dy
        self.grav(game_map)
        if self.y < game_map.map[self.x]:
            self.x -= 1
        elif(self.x <0):
            exit(0)


    def grav(self, game_map):
        if(self.y) - 1 >= game_map.map[self.x]:
            self.dy = max((self.y - game_map.map[self.x])* -1 , self.dy-1)
        else:
            self.dy = 0

    def jump(self):
        onclick = False
        if onclick is True:
            self.dy = variables.JUMP_HEIGHT

