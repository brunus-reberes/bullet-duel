import curses
from windows import * 
from resources import *
import config

def main(stdscr):

    curses.curs_set(0)

    scene = Window(stdscr, config.window_width, config.window_heigth).inside_window()

    MainMenu(scene)
    
    stdscr.move(config.window_heigth + 1, config.window_width)

if __name__ == "__main__":
    #try:
        curses.wrapper(main)
    #except Exception as err:
    #    print(err.with_traceback())