# urbandictionary

Программа для постинга в [группу вконтакте](https://vk.com/urbandictionary) через определенный промежуток времени. Постим  карточки со сленговыми словами из сайта [urabandictionary](https://urbandictionary.com). Проект написан на python v3.8, использованы библиотеки: pillow, bs4, requests. Проект взаимодейтвует с api 2-ух сайтов: [vk.com] и [urbandictionary.com].


# Терминология проекта

**content** - контент - словарь с информацие о слове.

_Пример:_
```python
from get_content import get_content, get_random_word
content = get_content(get_random_word())
print(content)

{'author': 'AYB',
 'category': 'drugs',
 'current_vote': '',
 'defid': 71371,
 'definition': "[God's gift] to the world.  Brings [peace] when used [wisely].",
 'example': '[Pass the blunt], [dude].',
 'permalink': 'http://weed.urbanup.com/71371',
 'sound_urls': ['http://api.twilio.com/2008-08-01/Accounts/ACd09691b82112e4b26fce156d7c01d0ed/Recordings/REe6c49d88147ef1a36de6b0a4ed5caaaf',
                'http://wav.urbandictionary.com/weed-25778.wav',
                'http://wav.urbandictionary.com/weed-35157.wav',
                'http://wav.urbandictionary.com/weed-35455.wav',
                'http://wav.urbandictionary.com/weed-36021.wav',
                'http://wav.urbandictionary.com/weed-39468.wav'],
 'thumbs_down': 8134,
 'thumbs_up': 52653,
 'word': 'weed',
 'written_on': '2003-03-25T00:00:00.000Z'}
```

**card** - карточка - сверстанное из контента и шаблона изображение.

_Пример:_
![weed.png](https://github.com/AndrewPythonist/urbandictionary/raw/master/data/cards/weed.png)
# Структура проекта

+ data
  + cards - папка для хранения карточек
    + weed.png - пример карточки
  + datasets
    + allnames.txt - датасет для исключения имен в функции get_random_word из библиотеки get_content
  + template - шаблон карточки
    + backgroundimages - изображения для шаблона
    + fonts - все шрифты проекта
    + icons - иконки для верстки шаблона
+ lib - все основные программы проекта
  + other
    + text_wrap.py - вспомогательная программа, для разделения многострочных строк.
  + draw_card.py - программа для верстки карточки из шаблона и контента.
  + get_content.py - программа для нахождения контента.
  + wall_posting.py - программа для постинга в группу вк
+ main.py - запускающая программа, которая связывает все 3 основные программы из папки lib.
+ .gitignore
+ .README.md

