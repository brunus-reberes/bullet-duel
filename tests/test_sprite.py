import test

from bulletduel.resources.blueprint import Sprite
from bulletduel.resources.sprites.factory import get, menu


# test sprite factory
def print_sprite(name):
    sprite = get(name)
    print(sprite)


print_sprite("logo")
print_sprite("pointer_left")
print_sprite("pointer_right")

#test Menu
imenu = menu(['one', 'two', 'three'])
print(imenu)
