import requests
from pprint import pprint
print = pprint

params = {
    'access_token':'31802b74c1021cbbb27482ce9b137fd09b10c2fc2023e9c82583a8c06f09e2774f0a4654ca9c6ea7f0f68',
    'v':5.103,
    'group_id':191098332
}

upload_url = requests.get('https://api.vk.com/method/photos.getWallUploadServer', params = params).json()['response']['upload_url']

request = requests.post(upload_url, files = {'photo':open('plant mom.png', 'rb')}).json()


params = {
    'access_token':'31802b74c1021cbbb27482ce9b137fd09b10c2fc2023e9c82583a8c06f09e2774f0a4654ca9c6ea7f0f68',
    'v':5.103,
    'group_id':191098332,
    'photo':request['photo'],
    'server':request['server'],
    'hash':request['hash'],
}

photo = requests.get('https://api.vk.com/method/photos.saveWallPhoto', params = params).json()['response'][0]

data = {
    'access_token':'31802b74c1021cbbb27482ce9b137fd09b10c2fc2023e9c82583a8c06f09e2774f0a4654ca9c6ea7f0f68',
    'v':5.103,
    'owner_id':-191098332,
    'from_group':1,
    'message':'',
    'attachments':f"photo{photo['owner_id']}_{photo['id']}"
}

req = requests.get('https://api.vk.com/method/wall.post', params = data)

print(req.json())

