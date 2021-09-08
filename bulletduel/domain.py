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


class Sprite:

    @staticmethod
    def clean(image: str) -> str:
        image_striped = image.splitlines()
        image_cleaned = list()
        for strip in image_striped:
            if not (strip == '' or strip.isspace()):
                image_cleaned.append(strip)
        return image_cleaned


    def __init__(self, image, y, x) -> None:
        self.image = self.clean(image)
        self.y = y
        self.x = x

    def print(self, stdscr):
        pass

    def erase(self, stdscr):
        pass


        

if __name__ == '__main__':
    s = '''
         .
    <===<>}-;
         ´
         '''

    s = Sprite.clean(s)
    print(s)
