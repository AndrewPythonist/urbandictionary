from PIL import Image, ImageDraw, ImageFont
from getcontent import search, get_random_word
from text_wrap import text_wrap
from datetime import datetime
from generategradient import random_gradient
from pprint import pprint

class DrawCard():

    def __init__(self,word = False, image = False):
        '''
        If image specifi then use concrect image, eles use random gradient
        '''
        self.content = search(word) if word else search(get_random_word())
        self.image = Image.open(image) if image else random_gradient()    
        self.set_fonts()
        self.image = self.image.resize(self.__image_size())
        self.set_size()
        self.draw = ImageDraw.Draw(self.image, 'RGBA')

    def __image_size(self):
        self.__def_lines = text_wrap(self.content['definition'],self.__def_font, 556*2)
        self.__ex_lines = text_wrap(self.content['example'],self.__ex_font, 556*2)
        
        width = 620*2
        height = 32*2 + 30*2 + 40*2 + 16*2 + len(self.__def_lines)*20*2 + 20*2 + len(self.__ex_lines)*16*2 + 16*2 + 20*2 + 40*2
        return width,height

    def set_size(self):
        '''Set up variables width and height of image.'''
        self.width = self.image.size[0]
        self.height = self.image.size[1]

    def get_size(self):
        '''Print width and height of image.'''
        print(f'width - {self.width}; height - {self.height}')

    def set_fonts(self):
        self.__rect_font = ImageFont.truetype('fonts/SourceSansPro-Semibold.otf', size=13*2)
        self.__word_font = ImageFont.truetype('fonts/Lora-Bold.ttf', size=32*2)
        self.__cat_font = ImageFont.truetype('fonts/SourceSansPro-Regular.otf', size=16*2)
        self.__def_font = ImageFont.truetype('fonts/SourceSansPro-Regular.otf', size=16*2)
        self.__ex_font = ImageFont.truetype('fonts/SourceSansPro-It.otf', size=16*2)
        self.__aut_font = ImageFont.truetype('fonts/SourceSansPro-Semibold.otf', size=16*2)

    def get_content(self):
        for item in ['word','definition','example']:
            print(self.content[item])

    def show(self):
        self.image.show()

    def save(self):
        word = self.content['word']

        for item in '[\/:*?"<>|]':
            word = word.replace(item, "")

        filepath = f"cards/{word}.png"
        self.image.save(filepath, format = 'PNG')
        
        return filepath

    def __draw_template(self):

        def yellow_rectangle():
            self.draw.rectangle((32*2, 32*2, 32*2+90*2, 32*2+16*2), fill=(239,255,0))
            self.draw.text((32*2,33*2), font = self.__rect_font, text = 'TOP DEFINITION', fill='#333333')

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
        
        def category():
            if self.content['category'] == "":
                pass
            else:
                colors = {'college':'#00ffbb', 'drugs':'#00ff2f', 'food':'#eaff00', 'music':'#ff008c', 'sex':'red'}

                width, height = self.__cat_font.getsize(self.content['category'])
                self.draw.rectangle((self.width-32*2-6*2-width-6*2,55*2 ,self.width-32*2 , 55*2+height), fill=colors[self.content['category']])                
                self.draw.text((self.width-32*2-6*2-width,55*2-2*2), text = self.content['category'], font = self.__cat_font, fill='#FFFFFF')

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
            category()
            thumbs()
            text_right()

        template()

    def __draw_text(self):

        def set_word():
            self.draw.text((32*2,55*2), text = self.content['word'], font = self.__word_font, fill='#134FE6')

        def set_definition():
            line_height = self.__def_font.getsize('hg')[1]

            space = 0
            for line in self.__def_lines:
                self.draw.text((32*2, 32*2+25*2+40*2+16*2+space), text = line, font = self.__def_font, fill="#2C353C")
                space += line_height

        def set_example():
            line_height = self.__ex_font.getsize('hg')[1]

            space = 0
            for line in self.__ex_lines:
                self.draw.text((32*2, 32*2+25*2+40*2+16*2+len(self.__def_lines)*line_height+16*2+space), text = line, font = self.__ex_font, fill="#2C353C")
                space += line_height

        def set_author():
            date = datetime.strftime(datetime.strptime(self.content['written_on'][:10], "%Y-%m-%d"), "%B %d,%Y")
            y = 32*2+25*2+40*2+16*2+len(self.__def_lines)*19.5*2+16*2 + len(self.__ex_lines)*19.5*2 + 15*2
            self.draw.text((32*2, y), text = f"by {self.content['author']} {date}", font = self.__aut_font, fill="#333333")

        def text():
            set_word()
            set_definition()
            set_example()
            set_author()

        text()
    
    def draw_card(self):
        self.__draw_template()
        self.__draw_text()

def test():
    for i in range(1,11):  
        image = DrawCard('banana',image = f"themes/gradient ({i}).jpg")
        image.draw_card()
        image.save({i})

if __name__ == '__main__':
    test()