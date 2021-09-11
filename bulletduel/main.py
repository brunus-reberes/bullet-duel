import curses
from windows import * 
from resources import *
import config

def main(stdscr):

    Window(stdscr, config.window_width, config.window_heigth)

    MainMenu(stdscr)
    
    stdscr.move(config.window_heigth + 1, config.window_width)
    stdscr.getkey()

if __name__ == "__main__":
    #try:
        curses.wrapper(main)
    #except Exception as err:
    #    print(err.with_traceback())