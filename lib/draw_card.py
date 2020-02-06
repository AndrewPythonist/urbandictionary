from PIL import Image, ImageDraw, ImageFont
from lib.get_content import get_content
from lib.other.text_wrap import text_wrap
from datetime import datetime

class DrawCard():

    def __init__(self, word, image):
        self.content = get_content(word)
        self.image = Image.open(image)
        self.__set_fonts()
        self.__set_size()
        self.draw = ImageDraw.Draw(self.image, 'RGBA')

    def __set_fonts(self):
        '''Передает в переменные шрифты формата ImageFont.'''
        self.__rect_font = ImageFont.truetype('data/template/fonts/SourceSansPro-Semibold.otf', size=13*2)
        self.__word_font = ImageFont.truetype('data/template/fonts/Lora-Bold.ttf', size=32*2)
        self.__cat_font = ImageFont.truetype('data/template/fonts/SourceSansPro-Regular.otf', size=16*2)
        self.__def_font = ImageFont.truetype('data/template/fonts/SourceSansPro-Regular.otf', size=16*2)
        self.__ex_font = ImageFont.truetype('data/template/fonts/SourceSansPro-It.otf', size=16*2)
        self.__aut_font = ImageFont.truetype('data/template/fonts/SourceSansPro-Semibold.otf', size=16*2)

    def __set_size(self):
        '''Функция вычисляет размер изображения, исходя из контента и шрифтов,
        изменяет размер изображения, и передает ширину и высоту в переменные.
        '''
        self.__def_lines = text_wrap(self.content['definition'],self.__def_font, 556*2)
        self.__ex_lines = text_wrap(self.content['example'],self.__ex_font, 556*2)
        width = 620*2
        height = 32*2 + 30*2 + 40*2 + 16*2 + len(self.__def_lines)*20*2 + 20*2 + len(self.__ex_lines)*16*2 + 16*2 + 20*2 + 40*2
        self.image = self.image.resize((width, height))

        self.width = self.image.size[0]
        self.height = self.image.size[1]

    def get_size(self):
        '''Print width and height of image.'''
        print(f'width - {self.width}; height - {self.height}')

    def get_content(self):
        '''Функция для печати выборочных частей контента.'''
        for item in ['word','definition','example']:
            print(self.content[item])

    def show(self):
        '''Функция для просмотра изображения'''
        self.image.show()

    def save(self, filepath='data/cards/', filename=None):
        '''Метод для сохранения изображения,
        filename - папка для сохранения, по умолчанию cards/
        filename - название для изображения, по умолчанию слово из контента.
        '''

        if filename is None:
            filename = self.content['word']

        for item in '[\\/:*?"<>|]':
            filename = filename.replace(item, "")

        path = f"{filepath}{filename}.png"
        self.image.save(path, format = 'PNG')
        
        return path

    def delete(self):
        '''Метод для удаления изображения'''
        pass
    
    def __draw_template(self):

        def yellow_rectangle():
            self.draw.rectangle((32*2, 32*2, 32*2+90*2, 32*2+16*2), fill=(239,255,0))
            self.draw.text((32*2,33*2), font = self.__rect_font, text = 'TOP DEFINITION', fill='#333333')

        def social_icons():

            twitter = Image.open('data/template/logos/twitter.png')
            twitter = twitter.resize((16*2,16*2))
            self.image.paste(twitter, (self.width-32*2-16*2-15*2-16*2-15*2-16*2,32*2), mask=twitter)

            facebook = Image.open('data/template/logos/facebook.png')
            facebook = facebook.resize((16*2,16*2))
            self.image.paste(facebook, (self.width-32*2-16*2-15*2-16*2,32*2), mask=facebook)

            links = Image.open('data/template/logos/link.png')
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
            border = Image.open('data/template/logos/border.png').convert("RGBA")
            border = border.resize((144*2,40*2))
            self.image.paste(border, (32*2,self.height-40*2-5*2), mask = border)

            font = ImageFont.truetype('data/template/fonts/SourceSansPro-Semibold.otf', size=12*2) # убрать шрифт наверх
            self.draw.text((32*2+16*2+16*2+8*2, self.height-5*2-29*2),fill="#000000", text = str(self.content['thumbs_up']), font= font)
            self.draw.text((32*2+75*2+8*2+16*2+6.5*2, self.height-5*2-29*2),fill="#000000", text = str(self.content['thumbs_down']), font= font)

        def text_right():

            flag = Image.open('data/template/logos/flag.png').convert("RGBA")
            flag = flag.resize((40*2,40*2))
            self.image.paste(flag,(self.width-32*2-40*2-40*2,self.height-40*2-5*2), mask = flag)

            dots = Image.open('data/template/logos/dots.png').convert("RGBA")
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

def save_card(word, image, filepath='data/cards/', filename=None):
    '''Функция для генерации и сохранения изображения
    Возвращает filepath+filename
    
    Параметры:
    word - слово, чей контент будет на карточке
    image - задний фон изображения
    filepath - путь для хранения изображения
    filename - имя изображения
    '''

    image = DrawCard(word = word, image = image)
    image.draw_card()
    path = image.save(filepath=filepath, filename=filename)

    return path

def test_draw_card():
    from get_content import get_random_word
    from pprint import pprint
    from random import randint

    image = DrawCard(word = get_random_word(), image = f'data/template/themes/gradient ({randint(1,10)}).jpg')
    image.get_content()
    image.draw_card()
    image.show()

if __name__ == '__main__':
    test_draw_card()