import time

from src.common.logger import get_logger
from src.singleton.the import The

logger = get_logger(__name__)


class UrbanDictionary:
    def __init__(self):
        logger.warning("starting UrbanDictionary")
        self.the = The()
        self.the.start_services()
        self.main_loop()

    @staticmethod
    def main_loop():
        """
        loop for every 1 second
        """
        logger.info("main_loop init")

        while True:
            time.sleep(1)
