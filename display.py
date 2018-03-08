"""Abstract away the system and allow us to work nicely with the display
as if it were a good canvas"""
from sys import stdout
import variables
def display(score, game_map, player):
    """Display the gamestate in the user's terminal"""
    for line in range(0, variables.MAP_HEIGHT+1):
        if line == 0:
            score_text = "score: " + str(score)
            for character in range(0, variables.MAP_WIDTH - len(score_text) + 1):
                stdout.write(' ')
            stdout.write(score_text)
        else:
            for character in range(0, variables.MAP_WIDTH):
                if (player.y == (variables.MAP_HEIGHT - line)
                    and player.x == character):
                    stdout.write('@')
                elif game_map[character] > (15 - line):
                    stdout.write('#')
                else:
                    stdout.write(' ')
        stdout.write("\r\n")
