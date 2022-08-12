import resources.button as button
from resources.blueprint import Menu, Window
from resources.sprites.factory import (logo, pointer_left,
                                                  pointer_right)


class MainMenu(Window):
    def setup(self) -> None:
        self.logo = logo()
        self.logo.x = self.win_width_mid - int(self.logo.width / 2)
        self.logo.y = 3

        self.menu = Menu(["Duel", "Campaign", "Rankings", "Settings", "Exit"])
        self.menu.x = self.win_width_mid - int(self.menu.width / 2)
        self.menu.y = 15

        self.left_pointer = pointer_right()
        self.left_pointer.x = self.menu.x - 3 - self.left_pointer.width
        self.left_pointer.y = 14

        self.right_pointer = pointer_left()
        self.right_pointer.x = self.menu.x + self.menu.width + 3 
        self.right_pointer.y = 14

    def run(self):
        y_min = 14
        y_max = 17
        self.logo.draw(self.stdscr)
        self.menu.draw(self.stdscr)
        self.left_pointer.draw(self.stdscr)
        self.right_pointer.draw(self.stdscr)
        while True:
            c = self.stdscr.getch()
            if c == ord("q"):
                break
            elif c == button.KEY_UP and self.left_pointer.y > y_min:
                self.left_pointer.move(self.stdscr, 0, -1)
                self.right_pointer.move(self.stdscr, 0, -1)
            elif c == button.KEY_DOWN and self.left_pointer.y < y_max:
                self.left_pointer.move(self.stdscr, 0, +1)
                self.right_pointer.move(self.stdscr, 0, +1)
            elif c == button.KEY_ENTER:
                break
