import bulletduel.resources.blueprint as blueprint
import bulletduel.resources.sprites.logos as logos


class Big(blueprint.Sprite):
    def __init__(self) -> None:
        super().__init__(logos.big)
