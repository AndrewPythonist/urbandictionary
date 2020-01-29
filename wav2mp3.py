from getcontent import search, get_random_word
import requests
from pydub import AudioSegment

from pprint import pprint

words = ['Sharkeisha']


content = search('doge')
pprint(content['sound_urls'])

def save_audio(audio_url):
    with open('audios/doge.wav', 'wb') as file:
        audio = requests.get(audio_url)
        file.write(audio.content)

# save_audio(content['sound_urls'][1])

# audio = AudioSegment.from_wav("audios/doge.wav")
# audio.export("audios/doge.mp3", format="mp3")




