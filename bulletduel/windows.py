import curses

class Window:

    def __init__(self, stdscr, width, height, top_bottom = '-', left_right = '|', corners = '+') -> None:
        self.stdscr = stdscr
        self.width = width
        self.height = height
        self.top_bottom = top_bottom
        self.left_right = left_right
        self.corners = corners
        self.print()

    def print(self):
        try:
            self.stdscr.clear()

            #TOP_BOTTOM
            for x in range(1, self.width - 1):
                self.stdscr.addch(0, x, self.top_bottom) #TOP
                self.stdscr.addch(self.height - 1, x, self.top_bottom)

            #LEFT_RIGHT
            for y in range(1, self.height - 1):
                self.stdscr.addch(y, 0, self.left_right)
                self.stdscr.addch(y, self.width - 1, self.left_right)

            #CORNERS
            self.stdscr.addch(0, 0, self.corners)
            self.stdscr.addch(0, self.width - 1, self.corners)
            self.stdscr.addch(self.height - 1, 0, self.corners)
            self.stdscr.addch(self.height - 1, self.width - 1, self.corners)

            self.stdscr.refresh()
        except Exception:
            raise Exception("Resize Window")   

    def inside_window(self):
        return curses.newwin(self.height-2, self.width-2, 1, 1) 


class WindowBorderless:
    pass