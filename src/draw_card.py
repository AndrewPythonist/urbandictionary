from PIL import Image

from src import urbandictionary_api
from src.card.cardDrawer import CardDrawer
from src.card.cardModel import CardModel
from src.repository import Repository
from src.urbandictionary_api import get_random_word


def save_card(word, image_path, filepath='data/cards/', filename=None):
    '''Функция для генерации и сохранения изображения
    Возвращает filepath+filename
    
    Параметры:
    word - слово, чей контент будет на карточке
    image - задний фон изображения
    filepath - путь для хранения изображения
    filename - имя изображения
    '''

    content = urbandictionary_api.get_word_data(word)
    image = Image.open(image_path)
    rep = Repository()
    fonts = rep.fonts
    model = CardModel(
        content=content,
        image=image,
        auth_font=fonts.aut_font,
        cat_font=fonts.cat_font,
        def_font=fonts.def_font,
        ex_font=fonts.ex_font,
        rect_font=fonts.rect_font,
        word_font=fonts.word_font,
        thumb_font=fonts.thumb_font
    )

    card_drawer = CardDrawer(model)
    card_drawer.draw_card()
    path = card_drawer.save(filepath=filepath, filename=filename)

    return path


if __name__ == '__main__':
    from random import randint

    save_card(get_random_word(), f'data/template/backgroundimages/bgimg ({randint(1, 9)}).jpg')
