from PIL import Image, ImageDraw, ImageFont
from getdefinition import search, get_random_word
from test import text_wrap
import operator
import functools

class Draw_card():

    def __init__(self,word=get_random_word()):
        self.content = search(word)
        self.image = Image.open('themes/gradient2.jpg')
        self.image = self.image.resize(self.__image_size(self.content))
        self.draw = ImageDraw.Draw(self.image)

    def get_size(self):
        '''
        Set up variables width and height of image and print them.
        '''
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        print(f'width - {self.width}')
        print(f'height - {self.height}')

    def show(self):
        self.image.show()

    def __delete_symbols(self,text):
        return text.replace(']','').replace('[','').replace('\r', '')

    def __add_lines(self,text):
        for i in range(len(text)):
            if text[i] == "":
                text[i] = '\n'
        return text


    def __image_size(self,text):
        listmerge=lambda s: functools.reduce(operator.iadd, s, [])
        definition_lines = len(listmerge([text_wrap(text,ImageFont.truetype('fonts/SourceSansPro-Regular.otf', size=16*2),556*2)for text in self.__add_lines(self.__delete_symbols(text['definition']).split('\n'))]))
        example_lines = len(listmerge([text_wrap(text,ImageFont.truetype('fonts/SourceSansPro-It.otf', size=16*2),556*2)for text in self.__add_lines(self.__delete_symbols(text['example']).split('\n'))]))
        
        width = 620*2
        height = 32*2 + 30*2 + 40*2 + 16*2 + definition_lines*20*2 + 20*2 + example_lines*16*2 + 16*2 + 20*2 + 50*2
        return width,height

    def template(self):

        def yellow_rectangle():
            self.draw.rectangle((32*2, 32*2, 32*2+90*2, 32*2+16*2), fill='#EFFF00')
            font = ImageFont.truetype('fonts/SourceSansPro-Semibold.otf', size=13*2)
            self.draw.text((32*2,33*2), font = font, text = 'TOP DEFINITION', fill='#333333')

        def social_icons():

            twitter = Image.open('logos/twitter.png')
            twitter = twitter.resize((16*2,16*2))
            self.image.paste(twitter, (self.width-32*2-16*2-15*2-16*2-15*2-16*2,32*2), mask=twitter)

            facebook = Image.open('logos/facebook.png')
            facebook = facebook.resize((16*2,16*2))
            self.image.paste(facebook, (self.width-32*2-16*2-15*2-16*2,32*2), mask=facebook)

            links = Image.open('logos/link.png')
            links = links.resize((16*2,16*2))
            self.image.paste(links, (self.width-32*2-16*2,32*2), mask=links)
            
        def thumbs():
            border = Image.open('logos/border.png').convert("RGBA")
            border = border.resize((144*2,40*2))
            self.image.paste(border, (32*2,self.height-40*2-5*2), mask = border)

            font = ImageFont.truetype('fonts/SourceSansPro-Semibold.otf', size=12*2)
            self.draw.text((32*2+16*2+16*2+8*2, self.height-5*2-29*2),fill="#000000", text = str(self.content['thumbs_up']), font= font)
            self.draw.text((32*2+75*2+8*2+16*2+6.5*2, self.height-5*2-29*2),fill="#000000", text = str(self.content['thumbs_down']), font= font)

        def text_right():

            flag = Image.open('logos/flag.png').convert("RGBA")
            flag = flag.resize((40*2,40*2))
            self.image.paste(flag,(self.width-32*2-40*2-40*2,self.height-40*2-5*2), mask = flag)

            dots = Image.open('logos/dots.png').convert("RGBA")
            dots = dots.resize((40*2,40*2))
            self.image.paste(dots,(self.width-32*2-40*2,self.height-40*2-5*2), mask = dots)

        def template():
            yellow_rectangle()
            social_icons()
            thumbs()
            text_right()

        template()


    def text(self):

        def set_word(text):
            font = ImageFont.truetype('fonts/Lora-Bold.ttf', size=32*2)
            draw.text((32*2,55*2), font = font, text = self.content['word'], fill='#134FE6')

        def set_definition(text):
            pass

        def set_example():
            pass

        def set_author():
            pass

        def text():
            set_word()
            set_definition()
            set_example()
            set_author()

        text()
        


image = Draw_card('agh')#get_random_word())
# width - 1240 height - 664
image.get_size()
image.template()
image.show()