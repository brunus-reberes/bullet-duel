import logging

import resources.button as button
from resources.blueprint import Menu, Window
from resources.sprites.factory import logo, pointer_left, pointer_right
from resources.windows import Exit, InDevelopment

logger = logging.getLogger(__name__)


class MainMenu(Window):
    def setup(self) -> None:
        self.logo = logo()
        self.logo.x = self.win_width_mid - int(self.logo.width / 2)
        self.logo.y = 2

        self.options = [
            ("Duel", InDevelopment),
            ("Campaign", InDevelopment),
            ("Rankings", InDevelopment),
            ("Settings", InDevelopment),
            ("Exit", Exit),
        ]
        self.menu = Menu(self.stdscr, self.options)
        self.menu.sprite.x = self.win_width_mid - int(self.menu.sprite.width / 2)
        self.menu.sprite.y = 14

        self.left_pointer = pointer_right()
        self.left_pointer.x = self.menu.sprite.x - 3 - self.left_pointer.width
        self.left_pointer.y = 13

        self.right_pointer = pointer_left()
        self.right_pointer.x = self.menu.sprite.x + self.menu.sprite.width + 3
        self.right_pointer.y = 13

        # draw base image
        self.stdscr.clear()
        self.logo.draw(self.stdscr)
        self.menu.sprite.draw(self.stdscr)
        self.left_pointer.draw(self.stdscr)
        self.right_pointer.draw(self.stdscr)

    def run(self):
        c = self.stdscr.getch()
        if c == ord("q"):
            self.exit = True
        elif c == button.KEY_UP and self.menu.previous():
            self.left_pointer.move(self.stdscr, 0, -1)
            self.right_pointer.move(self.stdscr, 0, -1)
        elif c == button.KEY_DOWN and self.menu.next():
            self.left_pointer.move(self.stdscr, 0, +1)
            self.right_pointer.move(self.stdscr, 0, +1)
        elif c == button.KEY_ENTER:
            self.menu.select()
            self.refresh = True
