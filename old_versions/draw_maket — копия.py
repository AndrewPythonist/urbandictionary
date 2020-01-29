from PIL import Image, ImageDraw, ImageFont
from getdefinition import search, get_random_word
from test import text_wrap
from datetime import datetime
import operator
import functools
from pprint import pprint
print = pprint


def delete_symbols(text):
    return text.replace(']','').replace('[','').replace('\r', '')

def add_lines(text):
    for i in range(len(text)):
        if text[i] == "":
            text[i] = '\n'
            # text.insert(i+1, '\n')
    return text

def image_size(text):
    listmerge=lambda s: functools.reduce(operator.iadd, s, [])
    definition_lines = len(listmerge([text_wrap(text,ImageFont.truetype('fonts/SourceSansPro-Regular.otf', size=16*2),556*2)for text in add_lines(delete_symbols(text['definition']).split('\n'))]))
    example_lines = len(listmerge([text_wrap(text,ImageFont.truetype('fonts/SourceSansPro-It.otf', size=16*2),556*2)for text in add_lines(delete_symbols(text['example']).split('\n'))]))
    
    width = 620*2
    height = 32*2 + 30*2 + 40*2 + 16*2 + definition_lines*20*2 + 20*2 + example_lines*16*2 + 16*2 + 20*2 + 50*2
    return width,height


WORD = search(get_random_word())

# image = Image.new('RGB', (620,500), color = 'yellow')
image = Image.open('themes/gradient2.jpg')
image = image.resize(image_size(WORD))
draw = ImageDraw.Draw(image)

width = image.size[0]
height = image.size[1]

def delete_spaces(text):
    while '' in text:
        text.remove('')
    return text



def yellow_rectangle():
    draw.rectangle((32*2, 32*2, 32*2+93.45*2, 32*2+16*2), fill='#EFFF00')
    font = ImageFont.truetype('fonts/SourceSansPro-Semibold.otf', size=13*2)
    draw.text((32*2,33*2), font = font, text = 'TOP DEFINITION', fill='black')

def social_icons():
    twitter = Image.open('logos/twitter.png')
    twitter = twitter.resize((16*2,16*2))
    facebook = Image.open('logos/facebook.png')
    facebook = facebook.crop((83,108,468,450))
    facebook = facebook.resize((16*2,16*2))
    links = Image.open('logos/link.png')
    links = links.crop((0,0,33,36))
    links = links.resize((16*2,16*2))

    image.paste(twitter, (width-32*2-16*2-15*2-16*2-15*2-16*2,32*2), mask=twitter)
    image.paste(facebook, (width-32*2-16*2-15*2-16*2,32*2), mask=facebook)
    image.paste(links, (width-32*2-16*2,32*2), mask=links)

def word(text):
    font = ImageFont.truetype('fonts/Lora-Bold.ttf', size=32*2)
    draw.text((32*2,55*2), font = font, text = text['word'], fill='#134FE6') 


def definition(text):

    texts = delete_symbols(text['definition'])
    texts = texts.split('\n')
    texts = add_lines(texts)
    font = ImageFont.truetype('fonts/SourceSansPro-Regular.otf', size=16*2)

    lines = []
    for text in texts:
        lines.extend(text_wrap(text,font,556*2))

    # print(lines)

    line_height = font.getsize('hg')[1]

    space = 0
    for line in lines:
        draw.text((32*2, 32*2+25*2+40*2+16*2+space),fill="#2C353C", text = line, font= font)
        space = space + line_height

    return len(lines)

def example(text,count_lines):

    font = ImageFont.truetype('fonts/SourceSansPro-It.otf', size=16*2)

    texts = add_lines(delete_symbols(text['example']).split('\n'))

    lines = []
    for text in texts:
        lines.extend(text_wrap(text,font,556*2))

    line_height = font.getsize('hg')[1]

    space = 0
    for line in lines:
        x=32*2
        y=32*2+25*2+40*2+16*2+count_lines*line_height+16*2+space
        draw.text((x, y),fill="#2C353C", text = line, font= font)
        space = space + line_height

    return y+font.getsize('hg')[1]


def author(text,y):
    font = ImageFont.truetype('fonts/SourceSansPro-Semibold.otf', size=16*2)
    line_height = font.getsize('hg')[1]
    date = datetime.strftime(datetime.strptime(text['written_on'][:10], "%Y-%m-%d"), "%B %d,%Y")
    text = f"by {text['author']} {date}"
    draw.text((32*2, y+16*2),fill="#333333", text = text, font= font)

def thumbs(text):

    font = ImageFont.truetype('fonts/SourceSansPro-Semibold.otf', size=13*2)

    thumbs_up = text['thumbs_up']
    thumbs_down = text['thumbs_down']

    # border = Image.open('logos/border.png')
    # border = border.resize((130*2,40*2))
    # image.paste(border, (32*2,height-80), mask = border)

    plus = Image.open('logos/plus.png')
    plus = plus.resize((16*2,16*2))
    x = 32*2+16*2
    y = height-30*2
    image.paste(plus, (x,y), mask=plus)#(x+16*2+6.5*2, y+16*2-13*2)
    # draw.text((100,100),fill="#000000", text = thumbs_up, font= font)

    minus = Image.open('logos/minus.png')
    minus = minus.resize((16*2,16*2))
    x = 32*2+16*2+56*2
    y = height-30*2
    image.paste(minus, (x,y), mask=minus)
    # draw.text((x+16*2+6.5*2, y+16*2-13*2),fill="#000000", text = thumbs_down, font= font)

def main():

    yellow_rectangle()
    social_icons()
    word(WORD)
    lines = definition(WORD)
    y_coord = example(WORD, lines)
    author(WORD,y_coord)
    thumbs(WORD)

    image.show()

main()
