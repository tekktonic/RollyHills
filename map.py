import random
import globals

class Map:
    """Our map """
    def generate(self):
        self.map[0] = random.randrange(0,9)
        for i in range(1,globals.MAP_WIDTH):
            self.slice(i-1)

    def __init__(self):
        self.map = []



    def slice(self,prev):
        """Move the map to the left"""
        self.map[prev+1]= self.map[prev] + (random.randrange(0,globals.JUMP_HEIGHT) * random.randrange(-1,1))


