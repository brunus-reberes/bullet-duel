import logging

from resources.blueprint import Window

logger = logging.getLogger(__name__)


class Exit(Window):
    def setup(self) -> None:
        self.exit = True

    def run(self):
        logger.info("exit game")
