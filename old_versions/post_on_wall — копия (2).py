import requests
from pprint import pprint
print = pprint


class VkPhoto():

    def __init__(self):
        self.token = '31802b74c1021cbbb27482ce9b137fd09b10c2fc2023e9c82583a8c06f09e2774f0a4654ca9c6ea7f0f68'
        self.version = 5.103

    def get_save_url(self):
        params = {
            'access_token':self.token,
            'v':self.version,
            'group_id':191098332
        }

        return requests.get('https://api.vk.com/method/photos.getWallUploadServer', params = params).json()['response']['upload_url']

    def get_photo_info(self,url,image):

        return requests.post(url, files = {'photo':open(image, 'rb')}).json()

    def save_photo(self,photo_info):

        params = {
            'access_token':self.token,
            'v':self.version,
            'group_id':191098332,
            'photo':photo_info['photo'],
            'server':photo_info['server'],
            'hash':photo_info['hash'],
        }

        return requests.get('https://api.vk.com/method/photos.saveWallPhoto', params = params).json()['response'][0]

    def post_photo(self, photo):

        data = {
            'access_token':self.token,
            'v':self.version,
            'owner_id':-191098332,
            'from_group':1,
            'message':'',
            'attachments':f"photo{photo['owner_id']}_{photo['id']}"
        }

        response = requests.get('https://api.vk.com/method/wall.post', params = data)

        try:
            if response.json()['response']:
                print(f"Successful posting by id {response.json()['response']['post_id']}")
        except:
            if response.json()['error']:
                print(f"Error {response.json()['error']['error_code']} - {response.json()['error']['error_msg']}")

photo = VkPhoto()

url = photo.get_save_url()

info = photo.get_photo_info(url,'trollface.png')

vkphoto = photo.save_photo(info)

photo.post_photo(vkphoto)