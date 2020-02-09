from src.common.logger import get_logger
from src.singleton.the import The

logger = get_logger(__name__)


class UrbanDictionary:
    def __init__(self):
        logger.warning("starting UrbanDictionary")
        self.the = The()
        self.the.start_services()

        pass
