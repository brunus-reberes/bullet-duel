import core
import logos 
import pointers


class MainMenu:

    def __init__(self, logo : core.Sprite = logos.Big(), pointers : core.Pointer = pointers.Swords()) -> None:
        self.logo = logo
        self.pointers = pointers
        self.print()


    def print(self, stdscr):

        self.logo.draw(stdscr, 3, 20)

        #este metodo tem de devolver uma sprite para depois poder ser desenhada
        menu = core.Sprite.compensate(['I Player', 'II Players', 'Options', 'Exit'])

        self.draw(stdscr, menu, 15, 20)

        menu_width = self.width(menu)
        pointers_width = self.width(self.pointers.left())

        self.drawr(stdscr, self.pointers.left(), 14, 20 - 3 - pointers_width)
        self.drawr(stdscr, self.pointers.right(), 14, 20 + 3 + menu_width)












