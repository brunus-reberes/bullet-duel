import utils
import sprites.logos 
import sprites.pointers

class MainMenu:

    def __init__(self, logo = sprites.logos.logo1, pointers = sprites.pointers.Swords()) -> None:
        self.logo = logo
        self.pointers = pointers
        self.print()


    def print(self, stdscr):
        utils.draw(stdscr, self.logo, 3, 20)

        menu = utils.compensate(['I Player', 'II Players', 'Options', 'Exit'])

        utils.draw(stdscr, menu, 15, 20)

        menu_width = utils.width(menu)
        pointers_width = utils.width(self.pointers.left())

        utils.drawr(stdscr, self.pointers.left(), 14, 20 - 3 - pointers_width)
        utils.drawr(stdscr, self.pointers.right(), 14, 20 + 3 + menu_width)












