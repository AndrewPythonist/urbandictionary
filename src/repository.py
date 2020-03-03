from src.fontContainer import FontContainer
from src.singleton.singleton import Singleton


class Repository(Singleton):
    __was_initialized = False

    def __init__(self):
        if not self.__was_initialized:
            self.__was_initialized = True

            self.fonts = FontContainer()
