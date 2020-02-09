from src.data.sets.base import DataSet
from src.services.baseService import BaseService


class DataSetService(BaseService):
    def __init__(self):
        self.name_data_set = DataSet()

    def load_data_sets(self):
        self.name_data_set.load_data("data/datasets/allnames.pickle")  # TODO add path to config

    def start(self):
        self.load_data_sets()
