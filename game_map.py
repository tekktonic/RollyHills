"""Generate and hold the game map"""
import random
import variables

class Map:
    """Our map """
    def generate(self):
        """Generate our initial map"""
        self.map.insert(0, random.randrange(0, 9))
        for i in range(1, variables.MAP_WIDTH):
            self.map.append(max(0, self.map[i-1]
                                + (random.randrange(0, variables.JUMP_HEIGHT)
                                   * random.randrange(-1, 2))))

    def __init__(self):
        self.map = []
        self.generate()


    def slice(self, prev):
        """Move the map to the left"""
        self.map[prev + 1] = max(0, min(10, self.map[prev]
                                 + ((random.randrange(-1, 2)
                                     * random.randrange(0, ((variables.JUMP_HEIGHT * (variables.JUMP_HEIGHT + 1)) / 2))))))

    def step(self):
        """"move all the array contents left by 1"""
        for i in range(1, variables.MAP_WIDTH):
            self.map[i-1] = self.map[i]
        self.slice(variables.MAP_WIDTH - 2)
