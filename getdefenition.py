import requests
from bs4 import BeautifulSoup
from pprint import pprint

# http://api.urbandictionary.com/v0/random #random request


def get_word_of_day():
    '''
    Return word of a day.
    '''
    html = requests.get('https://urbandictionary.com').text
    soup = BeautifulSoup(html,'lxml')
    return soup.find('a', {'class':'word'}).getText()


def search(word, value=1):
    '''
    Return a dict about a 'word' request; value - number of meanings of word.
    '''
    return eval(requests.get('http://api.urbandictionary.com/v0/define', params = {'term':word}).text)['list'][value-1]


if __name__ == '__main__':
    print(search(get_word_of_day()))


