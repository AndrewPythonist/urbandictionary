import requests
from bs4 import BeautifulSoup
from random import choice
from pprint import pprint
print = pprint

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

def get_random_word():
    '''
    Return a 'word'-object with a random wordfrom urbandictionary.
    '''

    return choice(requests.get('http://api.urbandictionary.com/v0/random').json()['list'])['word']

if __name__ == '__main__':
    print(search(get_random_word()))


