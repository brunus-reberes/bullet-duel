import curses
import logging

from config import window_height, window_width
from resources.blueprint import WindowFrame
from resources.windows.main_menu import MainMenu


def main(stdscr: curses.window):
    curses.curs_set(0)
    window = WindowFrame(stdscr, window_width, window_height).child_window()
    MainMenu(window)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    fh = logging.FileHandler("system.log")
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    logger.addHandler(fh)
    logger.addHandler(ch)
    try:
        logger.info("Starting game")
        curses.wrapper(main)
        logger.info("Exiting game")
    except Exception as err:
        logger.exception(err)
