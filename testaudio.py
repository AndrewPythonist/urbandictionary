from vktoken import token
import requests
from pprint import pprint

params = {
            'access_token':token,
            'v':5.103
        }


pprint(requests.get('https://api.vk.com/method/audio.getUploadServer', params = params).json())
upload_url = requests.get('https://api.vk.com/method/audio.getUploadServer', params = params).json()['response']['upload_url']

audio_info = requests.post(upload_url, files = {'file':open('audios/banana3.mp3', 'rb')}).json()

params = {
            'access_token':token,
            'v':5.103,
            'server':audio_info['server'],
            'audio':audio_info['audio'],
            'hash':audio_info['hash'],
            'artist':'urbandictionary',
            'title':'banana',
        }

response = requests.get('https://api.vk.com/method/audio.save', params = params)

pprint(response.json())