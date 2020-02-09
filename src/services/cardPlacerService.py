import threading
import time

from src import unbandictionary_api
from src.draw_card import save_card
from src.services.baseService import BaseService
from src.singleton.the import The
from src.wall_posting import posting
import random


class CardPlacerService(BaseService):
    def start(self):
        threading.Thread(name="card_placer_loop", target=self.place_loop).start()

    def __init__(self):
        pass

    @staticmethod
    def place_loop():
        the = The()

        token = the.config_service.data["token"].value
        group_id = the.config_service.data["group_id"].value
        album_id = the.config_service.data["album_id"].value
        sleep_for = the.config_service.data["time_span"].value
        names_data_set = the.data_set_service.name_data_set.data
        while True:
            word = unbandictionary_api.get_random_word()
            while word in names_data_set:
                word = unbandictionary_api.get_random_word()

            content = unbandictionary_api.get_content(word)

            path = save_card(
                word=word,
                image=f'data/template/backgroundimages/bgimg ({random.randint(1, 9)}).jpg'
            )

            posting(
                token=token,
                imagepath=path,
                group_id=group_id,
                album_id=album_id,
                message=f"#{content['category']}@urbandictionary" if content['category'] else ''
            )

            time.sleep(sleep_for)
