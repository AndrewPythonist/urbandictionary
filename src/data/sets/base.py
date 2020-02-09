from src.common import file


class DataSet:
    def __init__(self):
        self.data = None

    def load_data(self, path: str):
        self.data = file.unpickle_obj(path)

    def save_data(self, path: str):
        file.pickle_obj(self.data, path)

    def load_from_txt(self, path: str):
        f = open(path, "r")
        self.data = tuple([word.replace("\n", "").lower() for word in f if word != "\n"])
        f.close()

    def save_txt(self, path: str):
        f = open(path, "w")
        for data in self.data:
            f.write(data + "\n")
        f.close()
