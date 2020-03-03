from PIL.Image import Image


class CardModel:
    def __init__(self, content: dict, image: Image, word_font, rect_font, cat_font, def_font, ex_font, auth_font,
                 thumb_font):
        self.content = content
        self.image = image

        self.rect_font = rect_font
        self.word_font = word_font
        self.cat_font = cat_font
        self.def_font = def_font
        self.ex_font = ex_font
        self.aut_font = auth_font
        self.thumb_font = thumb_font
