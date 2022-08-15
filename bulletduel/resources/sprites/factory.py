from pathlib import Path

from resources.blueprint import Sprite


def get(name: str):
    with Path(__file__).parent.joinpath(name + ".txt").resolve().open("r") as file:
        sprite = file.read().splitlines()
    return Sprite(sprite)


def logo() -> Sprite:
    return get("logo")


def pointer_left() -> Sprite:
    return get("pointer_left")


def pointer_right() -> Sprite:
    return get("pointer_right")

def menu(options: list[str]) -> Sprite:
    highest_len = max([len(line) for line in options])
    new_options = []
    for line in options:
        spaces = " " * round((highest_len - len(line)) / 2)
        new_options.append(spaces + line)
    return Sprite(new_options)
