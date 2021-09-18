import curses


class Sprite:

    @staticmethod
    def clean(image: str) -> str:
        image_striped = image.splitlines()
        image_cleaned = list()
        for strip in image_striped:
            if not (strip == '' or strip.isspace()):
                image_cleaned.append(strip)
        return image_cleaned
    
    @classmethod
    def create_menu(cls, sprite):
        lens = [len(line) for line in sprite]
        highest_len = max(lens)
        new_sprite = ''
        for line in sprite:
            new_sprite += cls._compensate(line, highest_len) + '\n'
        return cls(new_sprite)

    @staticmethod
    def _compensate(line, highest_len):
        spaces = highest_len - len(line)
        half_spaces = round(spaces / 2)
        empty = ' ' * half_spaces
        line = empty + line
        return line


    def __init__(self, image, y = None, x = None) -> None:
        self.image = self.clean(image)
        self.y = y
        self.x = x
    
    @property
    def height(self):
        return len(self.image)
    
    @property
    def width(self):
        lens = [len(line) for line in self.image]
        return max(lens)

    def draw(self, stdscr, y, x):
        self.y = y
        self.x = x
        self._print(stdscr, self.image, y, x)

    def erase(self, stdscr):
        if not self.y is None and not self.x is None:
            self._print(stdscr, self._blank(), self.y, self.x)

    def _blank(self):
        blank = ' ' * self.width + '\n'
        return (blank * self.height).splitlines()

    def _print(self, stdscr, sprite, y, x):
        i = y
        for line in sprite:
            stdscr.addstr(i, x, line)
            i += 1
    

class Pointer:

    def __init__(self, right, left) -> None:
       self.right = Sprite(right)
       self.left = Sprite(left)

    def draw_left(self, stdscr, y, x):
       self.left.draw(stdscr, y, x)

    def erase_left(self, stdscr):
       self.left.erase(stdscr)
    
    def draw_right(self, stdscr, y, x):
       self.right.draw(stdscr, y, x)

    def erase_right(self, stdscr):
       self.right.erase(stdscr)


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


class Menu:

    def __init__(self, options: set, pointer: Pointer = None) -> None:
        pass


if __name__ == '__main__':
    import curses
    def main(stdscr):

        sword_left='''
   .
;-{<>===>
   `'''
        s = Sprite(sword_left)
        s.draw(stdscr, 0, 0)

        stdscr.refresh()
        stdscr.getkey()

        s.erase(stdscr)

        stdscr.refresh()
        stdscr.getkey()

    curses.wrapper(main)