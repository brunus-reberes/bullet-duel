import resources.button as button
from resources.blueprint import Window, WindowFrame, Menu
from resources.sprites.factory import logo, pointer_left, pointer_right
import curses
import logging
logger = logging.getLogger(__name__)


class InDevelopment(Window):
    def setup(self) -> None:
        width = 20
        height = 6
        logger.info(self.win_height_mid)
        new_stdscr = curses.newwin(
            height,
            width,
            self.win_height_mid - int(height / 2),
            self.win_width_mid - int(width / 2),
        )
        new_stdscr.border()
        logger.info(new_stdscr.getmaxyx())

    def run(self):
        self.stdscr.clear()
        self.stdscr.addstr(1, 2, "IN DEVELOPMENT!!!")
        self.stdscr.addstr(2, 2, "Click any key to continue")
        self.stdscr.getch()
        self.stdscr.clear()
