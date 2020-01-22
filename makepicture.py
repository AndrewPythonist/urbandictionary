from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from getdefinition import search, get_random_word

class Text():

    def __init__(self, file, definition):
        self.image = Image.open(file)
        self.image = self.image.resize((500,300))
        self.idraw = ImageDraw.Draw(self.image)
        self.definition = definition

    def __make_text(self,x,y,text,size,fill,font = "fonts/arial.ttf"):
        text = text
        font = ImageFont.truetype(font, size=size)
        self.idraw.multiline_text((x,y), text, font=font, fill = fill)

    def set_heading(self):
        '''Write heading'''
        self.__make_text(30, 20, self.definition['word'], 45, fill='black', font = 'fonts/Bangers-Regular.ttf')

    def set_definition(self):
        '''Write definition'''
        self.definition['definition'] = '\n'.join(wrap(definition['definition'], width=50))
        self.__make_text(30,80,definition['definition'],15, fill='black', font = 'fonts/Gelasio-Regular.ttf')

    def set_example(self):
        '''Write example'''
        self.definition['example'] = '\n'.join(wrap(definition['definition'], width=50))
        self.__make_text(30,200,definition['example'], 15, fill='black', font = 'fonts/Gelasio-Regular.ttf')

    def show(self):
        '''Func for show the image'''
        self.image.show()

if __name__ == "__main__":
    
    definition = search(get_random_word())
    text = Text('themes/gradient2.jpg', definition)

    text.set_heading()
    text.set_definition()
    text.set_example()
    text.show()