import exceptions


class Image:

    def _height(self, image):
        return len(image)
    
    def _width(self, image):
        lens = [len(line) for line in image]
        return max(lens)

    def draw(self, stdscr, sprite, y, x):
        i = y
        for line in sprite:
            stdscr.addstr(i, x, line)
            i += 1

    def drawr(self, stdscr, sprite, y, x):
        self.draw(stdscr, sprite, y, x)
        stdscr.refresh()

    def compensate(self, sprite):
        lens = [len(line) for line in sprite]
        highest_len = max(lens)
        return [self._compensate(line, highest_len) for line in sprite]

    def _compensate(self, line, highest_len):
        spaces = highest_len - len(line)
        half_spaces = round(spaces / 2)
        empty = ' ' * half_spaces
        line = empty + line
        return line


class Sprite(Image):

    @staticmethod
    def clean(image: str) -> str:
        image_striped = image.splitlines()
        image_cleaned = list()
        for strip in image_striped:
            if not (strip == '' or strip.isspace()):
                image_cleaned.append(strip)
        return image_cleaned


    def __init__(self, image) -> None:
        self.image = self.clean(image)
    
    @property
    def height(self):
        return self._height(self.image)
    
    @property
    def width(self):
        return self._width(self.image)


    def print(self, stdscr, y, x):
        self.y = y
        self.x = x
        self.draw(stdscr, self.image, y, x)

    def erase(self, stdscr):
        if not self.y or not self.x:
            raise exceptions.EreaseException('You must print sprite before erasing')
        self.draw(stdscr, self._blank(self.image), self.y, self.x)

    def _blank(self):
        blank = ' ' * self.width + '\n'
        return (blank * self.height).splitlines()
            

class Menu(Image):
    pass  


class Pointer():
    


if __name__ == '__main__':
    pass