from PIL import Image, ImageDraw, ImageFont
from lib.get_content import get_random_word, get_content

def text_wrap(text, font, width = 450):

    def delete_symbols(text):
        return text.replace(']','').replace('[','').replace('\r', '')

    def add_lines(text):
        for i in range(len(text)):
            if text[i] == "":
                text[i] = '\n'
        return text

    def wrap_line(text, font, width):
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

    text = add_lines(delete_symbols(text).split('\n'))

    lines = []

    for i in text:
        lines.extend(wrap_line(i,font,width))

    return lines

def main():
    content = search(get_random_word())
    print(content['word'])
    A = text_wrap(content['definition'],ImageFont.truetype('fonts/SourceSansPro-Regular.otf', size=16*2),556*2)
    print(A)

if __name__ == '__main__':
    main()