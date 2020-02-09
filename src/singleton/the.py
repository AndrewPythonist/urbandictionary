from src.services.configService import ConfigService
from src.singleton.singleton import Singleton

""""
Main handler of all services
"""


class The(Singleton):
    __was_initialized = False

    def __init__(self):
        """
        import here locally services, and create them
        """
        if not self.__was_initialized:
            self.__was_initialized = True

            self.services = {
                "config_service": ConfigService()
            }

    def start_services(self):
        for service in self.services:
            self.services[service].start()
