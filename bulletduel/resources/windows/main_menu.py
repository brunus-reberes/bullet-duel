import resources.button as button
from resources.blueprint import Window, Menu
from resources.sprites.factory import logo, pointer_left, pointer_right
from resources.windows.in_development import InDevelopment
import logging
logger = logging.getLogger(__name__)

class MainMenu(Window):
    def setup(self) -> None:
        self.logo = logo()
        self.logo.x = self.win_width_mid - int(self.logo.width / 2)
        self.logo.y = 2

        self.options = [
            ("Duel", InDevelopment(self.stdscr)),
            ("Campaign", InDevelopment(self.stdscr)),
            ("Rankings", InDevelopment(self.stdscr)),
            ("Settings", InDevelopment(self.stdscr)),
            ("Exit", None),
        ]
        self.menu = Menu(self.options)
        self.menu.sprite.x = self.win_width_mid - int(self.menu.sprite.width / 2)
        self.menu.sprite.y = 14

        self.left_pointer = pointer_right()
        self.left_pointer.x = self.menu.sprite.x - 3 - self.left_pointer.width
        self.left_pointer.y = 13

        self.right_pointer = pointer_left()
        self.right_pointer.x = self.menu.sprite.x + self.menu.sprite.width + 3
        self.right_pointer.y = 13

    def run(self):
        self.stdscr.clear()
        self.logo.draw(self.stdscr)
        self.menu.sprite.draw(self.stdscr)
        self.left_pointer.draw(self.stdscr)
        self.right_pointer.draw(self.stdscr)
        exit = False
        while not exit:
            c = self.stdscr.getch()
            if c == ord("q"):
                break
            elif c == button.KEY_UP and self.menu.previous():
                self.left_pointer.move(self.stdscr, 0, -1)
                self.right_pointer.move(self.stdscr, 0, -1)
            elif c == button.KEY_DOWN and self.menu.next():
                self.left_pointer.move(self.stdscr, 0, +1)
                self.right_pointer.move(self.stdscr, 0, +1)
            elif c == button.KEY_ENTER:
                exit = self.menu.select().start()
