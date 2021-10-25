import bulletduel.config as config
import bulletduel.resources.utilities.button as button
import bulletduel.resources.blueprint as blueprint
import bulletduel.resources.logos as logos
import bulletduel.resources.pointers as pointers


class MainMenu:

    def __init__(self, stdscr, logo : blueprint.Sprite = logos.Big(), pointers : blueprint.Pointer = pointers.Swords()) -> None:
        self.logo = logo
        self.logo_x = config.window_width_half - int(self.logo.width / 2)
        self.pointers = pointers
        self.menu = blueprint.Sprite.create_menu(['Duel', 'Campaign', 'Settings', 'Exit'])
        self.menu_x = config.window_width_half - int(self.menu.width / 2)

        self.start(stdscr)#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

    def start(self, stdscr):
        y_min = 14
        y_max = 17
        pointer_y = y_min
        while True:
            self.print(stdscr, pointer_y)
            c = stdscr.getch()
            if c == ord('q'):
                break 
            elif c == button.KEY_UP and pointer_y > y_min:
                pointer_y -= 1
            elif c == button.KEY_DOWN and pointer_y < y_max:
                pointer_y += 1
            elif c == button.KEY_ENTER:
                break

    def print(self, stdscr, pointer_y):

        self.logo.draw(stdscr, 3, self.logo_x)

        self.menu.draw(stdscr, 15, self.menu_x)

        self.pointers.erase_left(stdscr)
        self.pointers.draw_left(stdscr, pointer_y, self.menu.x - 3 - self.pointers.right.width)

        self.pointers.erase_right(stdscr)
        self.pointers.draw_right(stdscr, pointer_y, self.menu.x + 3 + self.menu.width)

        stdscr.refresh()










