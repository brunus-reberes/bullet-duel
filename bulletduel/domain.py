class Window:


    def __init__(self, width, height, top_bottom = '-', left_right = '|', corners = '+') -> None:
        self.width = width
        self.height = height
        self.top_bottom = top_bottom
        self.left_right = left_right
        self.corners = corners

    def print(self, stdscr):
        try:
            stdscr.clear()

            #TOP_BOTTOM
            for x in range(1, self.width - 1):
                stdscr.addch(0, x, self.top_bottom) #TOP
                stdscr.addch(self.height - 1, x, self.top_bottom)

            #LEFT_RIGHT
            for y in range(1, self.height - 1):
                stdscr.addch(y, 0, self.left_right)
                stdscr.addch(y, self.width - 1, self.left_right)

            #CORNERS
            stdscr.addch(0, 0, self.corners)
            stdscr.addch(0, self.width - 1, self.corners)
            stdscr.addch(self.height - 1, 0, self.corners)
            stdscr.addch(self.height - 1, self.width - 1, self.corners)

            stdscr.refresh()
        except Exception:
            raise Exception("Resize Window")            