'''Модуль содержит класс и методы для взаимодействия с api сайта vk.com.
Присутствуют методы загрузки и постинга на стену.
'''

import requests
from datetime import datetime


class VkPosting():
    '''VkPhoto class can upload and posting photo on vk group.'''

    def __init__(self, token):
        '''Initialize data to posting: token.'''

        self.token = token
        self.version = 5.103
        self.photo_info = None

    def __get_save_url(self, method):
        '''Helper function: get server url and save it in operator self.url
        Don't use this function
        '''
        if method == 'p':

            params = {
                'access_token': self.token,
                'v': self.version,
                'group_id': self.group_id,
                'album_id': self.album_id
            }

            return requests.get('https://api.vk.com/method/photos.getUploadServer', params=params).json()['response']['upload_url']

        elif method == 'a':

            params = {
                'access_token': self.token,
                'v': self.version
            }

            return requests.get('https://api.vk.com/method/audio.getUploadServer', params=params).json()['response']['upload_url']

    def upload_photo(self, imagefile, group_id, album_id):
        '''Upload photo to vk's servers and save self.photo_info about this image.
        Don't forget to write path to image!
        '''

        self.group_id = group_id
        self.album_id = album_id
        upload_url = self.__get_save_url('p')

        upload_info = requests.post(upload_url, files={'photo': open(imagefile, 'rb')}).json()

        params = {
            'access_token': self.token,
            'v': self.version,
            'group_id': self.group_id,
            'album_id': self.album_id,
            'photos_list': upload_info['photos_list'],
            'server': upload_info['server'],
            'hash': upload_info['hash'],
        }

        self.photo_info = requests.get('https://api.vk.com/method/photos.save', params=params).json()['response'][0]

    def upload_audio(self, audiofile, title):
        upload_url = self.__get_save_url('a')

        upload_info = requests.post(upload_url, files={'file': open(f'audios/{audiofile}', 'rb')}).json()

        params = {
            'access_token': token,
            'v': 5.103,
            'server': upload_info['server'],
            'audio': upload_info['audio'],
            'hash': upload_info['hash'],
            'artist': 'urbandictionary',
            'title': title
        }

        audio_info = requests.get('https://api.vk.com/method/audio.save', params=params).json()['response']

        return f",audio{audio_info['owner_id']}_{audio_info['id']}"

    def posting(self, message="", audio=""):
        '''Post photo uploaded with upload_photo. Take the group id from initialization.
        You can specify message that will post with image.
        '''

        if self.photo_info:

            data = {
                'access_token': self.token,
                'v': self.version,
                'owner_id': -self.group_id,
                'from_group': 1,
                'message': message,
                'attachments': (f"photo-{self.group_id}_{self.photo_info['id']}" + audio)
            }

            response = requests.get('https://api.vk.com/method/wall.post', params=data)

            try:
                if response.json()['response']:
                    print(f"{datetime.strftime(datetime.now(), '%X')} : Successful posting by id {response.json()['response']['post_id']}")
            except:
                if response.json()['error']:
                    print(
                        f"{datetime.strftime(datetime.now(), '%X')} : Error {response.json()['error']['error_code']} - {response.json()['error']['error_msg']}")
        else:
            print('ERROR: have no uploaded photo')


def posting(token, imagepath, group_id, album_id, message):
    post = VkPosting(token)
    post.upload_photo(imagepath, group_id, album_id)
    post.posting()


def test():
    from vk_info import token
    from pprint import pprint

    post = VkPosting(token)
    post.upload_photo('../data/cards/deez nuts.png', group_id=191098332, album_id=269851757)
    post.posting()


if __name__ == '__main__':
    test()
