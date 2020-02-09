import os

from src.common.logger import get_logger
from src.data.configData import ConfigData
from src.services.baseService import BaseService

logger = get_logger(__name__)


class ConfigService(BaseService):
    def __init__(self):
        self.data = {
            "token": ConfigData(str, ""),
            "group_id": ConfigData(int, 0),
            "album_id": ConfigData(int, 0),
            "time_span": ConfigData(int, 60)
        }

    def start(self):
        self.load_settings()

    def load_settings(self):
        if os.path.isfile("settings.cfg"):
            with open("settings.cfg", "r") as f:
                for line in f:
                    try:
                        line = line.replace("\n", "")
                        line = line.split("=")
                        config = line[0]
                        param = line[1]
                        self.set_data(config, param)
                    except Exception as e:
                        print("error", e)
        else:
            with open("settings.cfg", "a") as f:
                for key in self.data:
                    f.write(f"{key}={self.data[key].value}\n")

    def set_data(self, config: str, value):
        if config not in self.data:
            logger.exception(f"invalid config {config} type")
            return
        config_ = self.data[config]
        try:
            config_.set_value(value)
        except ValueError:
            logger.exception(f"invalid value {value} for config {config}, set default value")
            config_.set_value(config_.default_value)
