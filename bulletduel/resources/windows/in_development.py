import curses
import logging

import resources.button as button
from resources.blueprint import Menu, Window


class InDevelopment(Window):
    def setup(self) -> None:
        logger = logging.getLogger(self.__class__.__name__)
        logger.info("middle of window height: " + self.win_height_mid)
        logger.info("max y and x: " + new_stdscr.getmaxyx())
        width = 20
        height = 6
        new_stdscr = curses.newwin(
            height,
            width,
            self.win_height_mid - int(height / 2),
            self.win_width_mid - int(width / 2),
        )
        new_stdscr.border()

    def run(self):
        self.stdscr.clear()
        self.stdscr.addstr(1, 2, "IN DEVELOPMENT!!!")
        self.stdscr.addstr(2, 2, "Click any key to continue")
        self.stdscr.getch()
        self.stdscr.clear()
