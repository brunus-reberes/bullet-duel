import curses
import logging

from config import window_height, window_width
from resources.blueprint import WindowFrame
from resources.windows.main_menu import MainMenu


def main(stdscr: curses.window):
    logging.basicConfig(filename="system.log", filemode="w", level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    try:
        logger.info("starting game")

        curses.curs_set(0)
        window = WindowFrame(stdscr, window_width, window_height).child_window()
        MainMenu(window).start()

        logger.info("exiting game")
    except Exception as err:
        logger.exception(err)


if __name__ == "__main__":
    curses.wrapper(main)
