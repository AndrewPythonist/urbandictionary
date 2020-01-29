from PIL import Image, ImageDraw, ImageFont
from getdefinition import search, get_random_word
from test import text_wrap

# image = Image.new('RGB', (620,500), color = 'yellow')
image = Image.open('themes/gradient2.jpg')
image = image.resize((620,500))
draw = ImageDraw.Draw(image)

width = image.size[0]

def yellow_rectangle():
    draw.rectangle((32, 32, 32+93.45, 32+16), fill='#EFFF00')
    font = ImageFont.truetype('fonts/SourceSansPro-Semibold.otf', size=13)
    draw.text((32,33), font = font, text = 'TOP DEFINITION', fill='black')

def social_icons():
    twitter = Image.open('logos/twitter.png')
    twitter = twitter.resize((16,16))
    facebook = Image.open('logos/facebook.png')
    facebook = facebook.crop((83,108,468,450))
    facebook = facebook.resize((16,16))
    links = Image.open('logos/link.png')
    links = links.crop((0,0,33,36))
    links = links.resize((16,16))


    image.paste(twitter, (width-32-16-15-16-15-16,32), mask=twitter)
    image.paste(facebook, (width-32-16-15-16,32), mask=facebook)
    image.paste(links, (width-32-16,32), mask=links)

def word():
    font = ImageFont.truetype('fonts/Lora-Bold.ttf', size=32)
    draw.text((32,55), font = font, text = search(get_random_word())['word'], fill='#134FE6') 

def definition():
    definition = search(get_random_word())['definition']
    print(definition)

    font = ImageFont.truetype('fonts/SourceSansPro-ExtraLight.otf', size=16)
    lines = text_wrap(definition,font,556)
    print(lines)
    line_height = font.getsize('hg')[1]
    space = 0
    for line in lines:
        draw.text((32, 55+16+32+space),fill="#2C353C", text = line)
        space = space + line_height - 10

def main():

    yellow_rectangle()
    social_icons()
    word()
    definition()

    image.show()

main()