def draw(stdscr, sprite, y, x):
    i = y
    for line in sprite:
        stdscr.addstr(i, x, line)
        i += 1

def drawr(stdscr, sprite, y, x):
    draw(stdscr, sprite, y, x)
    stdscr.refresh()


def compensate(sprite):
    lens = [len(line) for line in sprite]
    highest_len = max(lens)
    return [_compensate(line, highest_len) for line in sprite]

def _compensate(line, highest_len):
    spaces = highest_len - len(line)
    half_spaces = round(spaces / 2)
    empty = ' ' * half_spaces
    line = empty + line
    return line

def height(sprite):
    return len(sprite)

def width(sprite):
    lens = [len(line) for line in sprite]
    return max(lens)

    



