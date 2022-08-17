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
