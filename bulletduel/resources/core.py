import exceptions


class Sprite():

    @staticmethod
    def clean(image: str) -> str:
        image_striped = image.splitlines()
        image_cleaned = list()
        for strip in image_striped:
            if not (strip == '' or strip.isspace()):
                image_cleaned.append(strip)
        return image_cleaned
    
    @staticmethod
    def compensate(sprite):
        lens = [len(line) for line in sprite]
        highest_len = max(lens)
        return [Sprite._compensate(line, highest_len) for line in sprite]

    @staticmethod
    def _compensate(line, highest_len):
        spaces = highest_len - len(line)
        half_spaces = round(spaces / 2)
        empty = ' ' * half_spaces
        line = empty + line
        return line


    def __init__(self, image) -> None:
        self.image = self.clean(image)
    
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
        if not self.y or not self.x:
            raise exceptions.EreaseException('You must draw sprite before erasing')
        self._print(stdscr, self._blank(self.image), self.y, self.x)

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

    def print_left(self, stdscr, y, x):
       self.left.print(stdscr, y, x)

    def erase_left(self, stdscr):
       self.left.erase(stdscr)
    
    def print_right(self, stdscr, y, x):
       self.right.print(stdscr, y, x)

    def erase_right(self, stdscr):
       self.right.erase(stdscr)


if __name__ == '__main__':
    pass