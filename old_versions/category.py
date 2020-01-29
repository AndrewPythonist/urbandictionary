from getcontent import search, get_random_word
from bs4 import BeautifulSoup
import requests

'''
Print category info, like drugs, name, college, religion
'''


def main():
    url = search('algebra')['permalink']
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    # for item in soup.findAll('span',{'class':'category'}):
    #     print(item.getText())

    for item in soup.findAll('span',{'class':'category'}):
        print(item.getText())
        if item.getText() in ['college', 'drugs', 'food','music', 'name', 'religion', 'sex', 'sports', 'work']:
            return item.getText()
    return 'QQQ'

if __name__ == '__main__':
    print(main())