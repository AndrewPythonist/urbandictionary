from get_content import get_random_word, get_content
from wall_posting import posting
from draw_card import save_card
from vk_info import token, group_id, album_id
from time import sleep
from random import randint

def main(timespan):
    '''Основная функция программы: Карточки посятся на стену каждые timespan секунд'''
    while True:
        word = get_random_word()
        content = get_content(word)

        path = save_card(
            word=word,
            image=f'themes/gradient ({randint(1,9)}).jpg'
            )

        posting(
            token=token,
            imagepath=path,
            group_id=group_id,
            album_id=album_id,
            message=f"#{content['category']}@urbandictionary" if content['category'] else ''
            )

        sleep(timespan)

if __name__ == '__main__':
    main(17280)