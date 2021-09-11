import core
import images.pointers as pointer


class Swords(core.Pointer):

   def __init__(self) -> None:
       super().__init__(pointer.sword_right, pointer.sword_left)
       
