import bulletduel.resources.blueprint as blueprint
import bulletduel.resources.images.pointers as pointer


class Swords(blueprint.Pointer):

   def __init__(self) -> None:
       super().__init__(pointer.sword_right, pointer.sword_left)
       
