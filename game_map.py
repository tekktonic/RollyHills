"""Generate and hold the game map"""
import random
import variables

class Map:
    """Our map """
    def generate(self):
        """Generate our initial map"""
        self.map.insert(0, random.randrange(0, 9))
        for i in range(1, variables.MAP_WIDTH):
            self.slice(i - 1)

    def __init__(self):
        self.map = []
        self.generate()


    def slice(self, prev):
        """Move the map to the left"""
        self.map.insert(prev + 1, (self.map[prev]
                              + (random.randrange(0, variables.JUMP_HEIGHT)
                                 * random.randrange(-1, 1))))
