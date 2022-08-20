import curses
import logging
from abc import abstractmethod
from typing import Type, Union

logger = logging.getLogger(__name__)


class Sprite:
    def __init__(self, image: list[str]) -> None:
        self.image = image
        # create blank image
        self.blank = []
        for line in self.image:
            self.blank.append(len(line) * " ")
        self.y = None
        self.x = None
        self.height = len(self.image)
        self.width = max([len(line) for line in self.image])

    def draw(self, stdscr: curses.window, y: int = None, x: int = None):
        self.y = self.y if y is None else y
        self.x = self.x if x is None else x
        for y, line in enumerate(self.image, self.y):
            try:
                stdscr.addstr(y, self.x, line)
            except Exception as e:
                import logging

                logger = logging.getLogger(__name__)
                logger.exception(e)

    def move(self, stdscr, width, height):
        self.erase(stdscr)
        self.y += height
        self.x += width
        self.draw(stdscr)

    def erase(self, stdscr: curses.window):
        if not self.y is None and not self.x is None:
            for y, line in enumerate(self.blank, self.y):
                stdscr.addstr(y, self.x, line)

    def __repr__(self) -> str:
        return "\n".join(self.image)


class WindowFrame:
    def __init__(
        self, stdscr, width, height, top_bottom="-", left_right="|", corners="+"
    ) -> None:
        self.stdscr: curses.window = stdscr
        self.width = width
        self.height = height
        self.top_bottom = top_bottom
        self.left_right = left_right
        self.corners = corners
        self.print()

    def print(self):
        try:
            self.stdscr.clear()
            # TOP_BOTTOM
            for x in range(1, self.width - 1):
                self.stdscr.addch(0, x, self.top_bottom)  # TOP
                self.stdscr.addch(self.height - 1, x, self.top_bottom)
            # LEFT_RIGHT
            for y in range(1, self.height - 1):
                self.stdscr.addch(y, 0, self.left_right)
                self.stdscr.addch(y, self.width - 1, self.left_right)
            # CORNERS
            self.stdscr.addch(0, 0, self.corners)
            self.stdscr.addch(0, self.width - 1, self.corners)
            self.stdscr.addch(self.height - 1, 0, self.corners)
            self.stdscr.addch(self.height - 1, self.width - 1, self.corners)
            # Print frame
            self.stdscr.refresh()
        except Exception:
            logger.error("could not print the window frame. try to resize terminal window")

    def child_window(self):
        return curses.newwin(self.height - 2, self.width - 2, 1, 1)


class Window:
    def __init__(self, stdscr: curses.window) -> None:
        self.win_height, self.win_width = stdscr.getmaxyx()
        self.win_width_mid = int(self.win_width / 2)
        self.win_height_mid = int(self.win_height / 2)
        self.stdscr = stdscr
        self.refresh = False
        self.exit = False

    def _run(self) -> None:
        while not self.exit:
            if self.refresh:
                self.setup()
                self.refresh = False
            self.run()

    @abstractmethod
    def setup() -> None:
        pass

    @abstractmethod
    def run() -> None:
        pass

    def start(self) -> bool:
        self.setup()
        self._run()

    def __repr__(self) -> str:
        return "'" + self.__class__.__name__ + "Window'"


class Menu:
    def __init__(self, stdscr: curses.window, options: list[(str, Type[Window])]) -> None:
        logger.info('initializing menu ' + str(options))
        self.names = []
        self.windows = []
        self.stdscr = stdscr
        self.logger = logging.getLogger(self.__class__.__name__)
        for name, win in options:
            self.names.append(name)
            self.windows.append(win)
        self.index = 1
        # build sprite
        highest_len = max([len(line) for line in self.names])
        new_options = []
        for line in self.names:
            spaces = " " * round((highest_len - len(line)) / 2)
            new_options.append(spaces + line)
        self.sprite = Sprite(new_options)

    def next(self) -> int:
        if self.index + 1 <= len(self.windows):
            self.index += 1
            self.logger.info('next item (index ' + str(self.index) + ')')
            return self.index

    def previous(self) -> int:
        if self.index - 1 >= 1:
            self.index -= 1
            self.logger.info('previous item (index ' + str(self.index) + ')')
            return self.index

    def select(self) -> Window:
        self.logger.info('selecting item (index ' + str(self.index) + ')')
        self.windows[self.index-1](self.stdscr).start()
