"""
Модуль содержит функции взаимодействия с api сайта urbandictionary.com
(присутствуют элементы парсинга)

Доступные функции:
get_content
get_random_word
"""

import requests
from bs4 import BeautifulSoup
from random import choice

# urls for api's method
DEFINE_URL = 'http://api.urbandictionary.com/v0/define'
RANDOM_URL = 'http://api.urbandictionary.com/v0/random'


def get_word_data(word: str, definition: int = 1) -> dict:
    """
    Функция возвращает словарь content c информацией о слове, параметры:
    word - слово которое нужно найти;
    definition - номер определения, по умолчанию 1-ое.
    """

    content_list = requests.get(DEFINE_URL, params={'term': word}).json()['list']

    if not content_list:
        raise Exception('Для этого слова нет определений.')

    content = content_list[definition - 1]

    # Добавляем ключ и значение категории в content,
    # если ее нет, категория - пустая строка.
    url = content['permalink']
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    for item in soup.findAll('span', {'class': 'category'}):
        if item.getText() in ['college', 'drugs', 'food', 'music', 'sex']:
            content['category'] = item.getText()
            break
        content['category'] = ""

    return content


def get_random_word() -> str:
    return choice(requests.get(RANDOM_URL).json()['list'])['word']


def test_get_content():
    from pprint import pprint
    print = pprint

    print(get_word_data(get_random_word()))


if __name__ == '__main__':
    test_get_content()
