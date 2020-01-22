import requests
import time as t


class VkPhoto():
    '''
    VkPhoto class can upload and posting photo on vk group.
    '''

    def __init__(self, token, group_id):
        '''
        Initialize data to posting: token, group_id.
        '''

        self.token = token
        self.group_id = group_id
        self.version = 5.103
        self.url = self.__get_save_url()
        self.photo_info = None

    def __get_save_url(self):
        '''
        helper function: get server url and save it in operator self.url
        Don't use this func
        '''

        params = {
            'access_token':self.token,
            'v':self.version,
            'group_id':self.group_id
        }

        return requests.get('https://api.vk.com/method/photos.getWallUploadServer', params = params).json()['response']['upload_url']

    def upload_photo(self,imagefile):
        '''
        Upload photo to vk's servers and save self.photo_info about this image.
        Don't forget to write path to image!
        '''

        photo_info = requests.post(self.url, files = {'photo':open(imagefile, 'rb')}).json()

        params = {
            'access_token':self.token,
            'v':self.version,
            'group_id':self.group_id,
            'photo':photo_info['photo'],
            'server':photo_info['server'],
            'hash':photo_info['hash'],
        }

        self.photo_info = requests.get('https://api.vk.com/method/photos.saveWallPhoto', params = params).json()['response'][0]

    def post_photo(self):
        '''
        Post photo uploaded with upload_photo. Take the group id from initialization.
        '''

        if self.photo_info:

            data = {
                'access_token':self.token,
                'v':self.version,
                'owner_id':-self.group_id,
                'from_group':1,
                'message':'',
                'attachments':f"photo{self.photo_info['owner_id']}_{self.photo_info['id']}"
            }

            response = requests.get('https://api.vk.com/method/wall.post', params = data)

            try:
                if response.json()['response']:
                    print(f"Successful posting by id {response.json()['response']['post_id']}")
            except:
                if response.json()['error']:
                    print(f"Error {response.json()['error']['error_code']} - {response.json()['error']['error_msg']}")
        else:
            print('ERROR: have no uploaded photo')


if __name__ == '__main__':

    photo = VkPhoto('31802b74c1021cbbb27482ce9b137fd09b10c2fc2023e9c82583a8c06f09e2774f0a4654ca9c6ea7f0f68',191098332)
    photo.upload_photo('happiest guy.png')

    for i in range(5,-1,-1):
        print(i)
        i-=1
        t.sleep(1)

    photo.post_photo()