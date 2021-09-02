import utils
from sprites.logos import logo1

class MainMenu:

    def print(self, stdscr):
        utils.draw(stdscr, logo1, 3, 20)

        menu = utils.compensate(['I Player', 'II Players', 'Options', 'Exit'])

        utils.drawr(stdscr, menu, 15, 10)









