import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.addstr(0, 0, str(curses.KEY_DOWN))
    stdscr.addstr(1, 0, str(curses.KEY_UP))
    stdscr.refresh()
    while True:
        c = stdscr.getch()
        stdscr.addstr(4, 0, ' ' * 4)
        stdscr.addstr(4, 0, str(c))
        stdscr.refresh()
        if c == ord('q'):
            break

curses.wrapper(main)