import curses
from domain import * 
import config

def main(stdscr):

    Window(config.window_width, config.window_heigth).print(stdscr)

    
    stdscr.getkey()



if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as err:
        print(err)