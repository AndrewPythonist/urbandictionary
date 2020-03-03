from datetime import datetime

from PIL import Image, ImageDraw

from src.card.cardModel import CardModel
from src.other.text_wrap import text_wrap


class CardDrawer:
    def __init__(self, model: CardModel):
        self.model = model
        self.image = model.image
        self.__set_size()
        self.draw = ImageDraw.Draw(self.image, 'RGBA')

    def __set_size(self):
        '''Функция вычисляет размер изображения, исходя из контента и шрифтов,
        изменяет размер изображения, и передает ширину и высоту в переменные.
        '''
        self.def_lines = text_wrap(self.model.content['definition'], self.model.def_font, 556 * 2)
        self.ex_lines = text_wrap(self.model.content['example'], self.model.ex_font, 556 * 2)
        width = 620 * 2
        height = 32 * 2 + 30 * 2 + 40 * 2 + 16 * 2 + len(self.def_lines) * 20 * 2 + 20 * 2 + len(
            self.ex_lines) * 16 * 2 + 16 * 2 + 20 * 2 + 40 * 2

        self.image = self.image.resize((width, height))

        self.width = self.image.size[0]
        self.height = self.image.size[1]

    def get_size(self):
        '''Print width and height of image.'''
        print(f'width - {self.width}; height - {self.height}')

    def get_content(self):
        '''Функция для печати выборочных частей контента.'''
        for item in ['word', 'definition', 'example']:
            print(self.model.content[item])

    def show(self):
        '''Функция для просмотра изображения'''
        self.image.show()

    def save(self, filepath='data/cards/', filename=None):
        '''Метод для сохранения изображения,
        filename - папка для сохранения, по умолчанию cards/
        filename - название для изображения, по умолчанию слово из контента.
        '''

        if filename is None:
            filename = self.model.content['word']

        for item in '[\\/:*?"<>|]':
            filename = filename.replace(item, "")

        path = f"{filepath}{filename}.png"
        self.image.save(path, format='PNG')

        return path

    def delete(self):
        '''Метод для удаления изображения'''
        pass

    def __draw_template(self):

        def yellow_rectangle():
            self.draw.rectangle((32 * 2, 32 * 2, 32 * 2 + 90 * 2, 32 * 2 + 16 * 2), fill=(239, 255, 0))
            self.draw.text((32 * 2, 33 * 2), font=self.model.rect_font, text='TOP DEFINITION', fill='#333333')

        def social_icons():

            twitter = Image.open('data/template/icons/twitter.png')
            twitter = twitter.resize((16 * 2, 16 * 2))
            self.image.paste(twitter, (self.width - 32 * 2 - 16 * 2 - 15 * 2 - 16 * 2 - 15 * 2 - 16 * 2, 32 * 2),
                             mask=twitter)

            facebook = Image.open('data/template/icons/facebook.png')
            facebook = facebook.resize((16 * 2, 16 * 2))
            self.image.paste(facebook, (self.width - 32 * 2 - 16 * 2 - 15 * 2 - 16 * 2, 32 * 2), mask=facebook)

            links = Image.open('data/template/icons/link.png')
            links = links.resize((16 * 2, 16 * 2))
            self.image.paste(links, (self.width - 32 * 2 - 16 * 2, 32 * 2), mask=links)

        def category():
            if self.model.content['category'] == "":
                pass
            else:
                colors = {'college': '#00ffbb', 'drugs': '#00ff2f', 'food': '#eaff00', 'music': '#ff008c', 'sex': 'red'}

                width, height = self.model.cat_font.getsize(self.model.content['category'])
                self.draw.rectangle(
                    (self.width - 32 * 2 - 6 * 2 - width - 6 * 2, 55 * 2, self.width - 32 * 2, 55 * 2 + height),
                    fill=colors[self.model.content['category']])
                self.draw.text((self.width - 32 * 2 - 6 * 2 - width, 55 * 2 - 2 * 2), text=self.model.content['category'],
                               font=self.model.cat_font, fill='#FFFFFF')

        def thumbs():
            border = Image.open('data/template/icons/border.png').convert("RGBA")
            border = border.resize((144 * 2, 40 * 2))
            self.image.paste(border, (32 * 2, self.height - 40 * 2 - 5 * 2), mask=border)

            self.draw.text((32 * 2 + 16 * 2 + 16 * 2 + 8 * 2, self.height - 5 * 2 - 29 * 2), fill="#000000",
                           text=str(self.model.content['thumbs_up']), font=self.model.thumb_font)
            self.draw.text((32 * 2 + 75 * 2 + 8 * 2 + 16 * 2 + 6.5 * 2, self.height - 5 * 2 - 29 * 2), fill="#000000",
                           text=str(self.model.content['thumbs_down']), font=self.model.thumb_font)

        def text_right():

            flag = Image.open('data/template/icons/flag.png').convert("RGBA")
            flag = flag.resize((40 * 2, 40 * 2))
            self.image.paste(flag, (self.width - 32 * 2 - 40 * 2 - 40 * 2, self.height - 40 * 2 - 5 * 2), mask=flag)

            dots = Image.open('data/template/icons/dots.png').convert("RGBA")
            dots = dots.resize((40 * 2, 40 * 2))
            self.image.paste(dots, (self.width - 32 * 2 - 40 * 2, self.height - 40 * 2 - 5 * 2), mask=dots)

        def template():
            yellow_rectangle()
            social_icons()
            category()
            thumbs()
            text_right()

        template()

    def __draw_text(self):

        def set_word():
            self.draw.text((32 * 2, 55 * 2), text=self.model.content['word'], font=self.model.word_font, fill='#134FE6')

        def set_definition():
            line_height = self.model.def_font.getsize('hg')[1]

            space = 0
            for line in self.def_lines:
                self.draw.text((32 * 2, 32 * 2 + 25 * 2 + 40 * 2 + 16 * 2 + space), text=line, font=self.model.def_font,
                               fill="#2C353C")
                space += line_height

        def set_example():
            line_height = self.model.ex_font.getsize('hg')[1]

            space = 0
            for line in self.ex_lines:
                self.draw.text(
                    (32 * 2, 32 * 2 + 25 * 2 + 40 * 2 + 16 * 2 + len(self.def_lines) * line_height + 16 * 2 + space),
                    text=line, font=self.model.ex_font, fill="#2C353C")
                space += line_height

        def set_author():
            date = datetime.strftime(datetime.strptime(self.model.content['written_on'][:10], "%Y-%m-%d"), "%B %d,%Y")
            y = 32 * 2 + 25 * 2 + 40 * 2 + 16 * 2 + len(self.def_lines) * 19.5 * 2 + 16 * 2 + len(
                self.ex_lines) * 19.5 * 2 + 15 * 2
            self.draw.text((32 * 2, y), text=f"by {self.model.content['author']} {date}", font=self.model.aut_font, fill="#333333")

        def text():
            set_word()
            set_definition()
            set_example()
            set_author()

        text()

    def draw_card(self):
        self.__draw_template()
        self.__draw_text()
