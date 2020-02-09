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

            from src.services.cardPlacerService import CardPlacerService
            from src.services.configService import ConfigService
            from src.services.dataSetService import DataSetService

            self.config_service = ConfigService()
            self.data_set_service = DataSetService()
            self.card_placer_service = CardPlacerService()

    def start_services(self):
        self.config_service.start()
        self.data_set_service.start()
        self.card_placer_service.start()
