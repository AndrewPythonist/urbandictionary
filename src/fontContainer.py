from PIL import ImageFont


class FontContainer:
    def __init__(self):
        self.rect_font = ImageFont.truetype('data/template/fonts/SourceSansPro-Semibold.otf', size=13 * 2)
        self.word_font = ImageFont.truetype('data/template/fonts/Lora-Bold.ttf', size=32 * 2)
        self.cat_font = ImageFont.truetype('data/template/fonts/SourceSansPro-Regular.otf', size=16 * 2)
        self.def_font = ImageFont.truetype('data/template/fonts/SourceSansPro-Regular.otf', size=16 * 2)
        self.ex_font = ImageFont.truetype('data/template/fonts/SourceSansPro-It.otf', size=16 * 2)
        self.aut_font = ImageFont.truetype('data/template/fonts/SourceSansPro-Semibold.otf', size=16 * 2)
        self.thumb_font = ImageFont.truetype('data/template/fonts/SourceSansPro-Semibold.otf', size=12 * 2)

