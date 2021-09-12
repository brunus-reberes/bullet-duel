class Sprite():

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
    

class Pointer():

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