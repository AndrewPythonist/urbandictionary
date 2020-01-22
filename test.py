from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from getdefinition import get_random_word, search

image = Image.open('themes/gradient2.jpg')
image = image.resize((500,500))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('fonts/Roboto.ttf', size=25)

line_height = font.getsize('hg')[1]

print(search(get_random_word()))

def text_wrap(text, font, width = 450):
    lines = []

    if font.getsize(text)[0] <= width:
        lines.append(text)
    else:
        words = text.split()
        i=0

        while i < len(words):
            line = ""

            while i < len(words) and font.getsize(line + words[i])[0] < width:
                line = f'{line}{words[i]} '
                i+=1
            if not line:
                line = words[i]
                i+=1
            lines.append(line)

    return lines

def main():

    text = 'The best greeting ever. Once said by Liza Minnelli, and reviewed by Ray William Johnson, has become the most formal greeting ever.'

    space = 0
    for line in text_wrap(text, font):
        draw.text((30,30+space), font= font, text = line)
        space +=line_height

    image.show()

main()