import core
import logos 
import pointers


class MainMenu(core.Menu):

    def __init__(self, logo = logos.Big(), pointers = pointers.Swords()) -> None:
        self.logo = logo
        self.pointers = pointers
        self.print()


    def print(self, stdscr):
        self.draw(stdscr, self.logo, 3, 20)

        menu = self.compensate(['I Player', 'II Players', 'Options', 'Exit'])

        self.draw(stdscr, menu, 15, 20)

        menu_width = self.width(menu)
        pointers_width = self.width(self.pointers.left())

        self.drawr(stdscr, self.pointers.left(), 14, 20 - 3 - pointers_width)
        self.drawr(stdscr, self.pointers.right(), 14, 20 + 3 + menu_width)












