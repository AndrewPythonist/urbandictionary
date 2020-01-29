from getcontent import get_random_word, search
from time import sleep
from wall_posting import VkPosting
from drawcard import DrawCard
from vktoken import token
import requests
from pydub import AudioSegment
from random import randint


def posting():
    image = DrawCard(get_random_word(),image = f'themes/gradient ({randint(1,10)}).jpg')
    image.draw_card()
    fileimage = image.save()

    post = VkPosting(token)
    post.upload_photo(fileimage, group_id = 191098332, album_id = 269851757)

    message = f"#{image.content['category']}@urbandictionary" if image.content['category'] else ''

    def audio():

        def save_audio(audio_url, filename):
            with open(f"audios/{filename}", 'wb') as file:
                audio = requests.get(audio_url)
                file.write(audio.content)

        if image.content['sound_urls']:

            word = image.content['word']
            for item in '[\/:*?"<>|]':
                word = word.replace(item, "")

            save_audio(image.content['sound_urls'][0], f'{word}.wav')

            AudioSegment.from_wav(f"audios/{word}.wav").export(f"audios/{word}.mp3", format="mp3")

            try:
                return post.upload_audio(f'{word}.mp3',image.content['word'])
            except:
                pass
        else:
            return ""

    post.posting(message = message)

def main():
    while True:
        posting()
        sleep(10800)

if __name__ == '__main__':
    main()