from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap

defenition = {'definition': 'mother of plants. someone who owns a significant number of plants and care for them deeply, these plants are usually kept inside to be close to their surrogate mother.', 'permalink': 'http://plant-mom.urbanup.com/12825565', 'thumbs_up': 1119, 'sound_urls': [], 'author': 'iwantdeathpls', 'word': 'plant mom\U0001f618', 'defid': 12825565, 'current_vote': '', 'written_on': '2018-05-25T00:00:00.000Z', 'example': "person 1: 'that person sure likes plants'\r\nperson 2:'yeh . she's a plant mom'", 'thumbs_down': 468}

image = Image.open('yellow.png')

idraw = ImageDraw.Draw(image)


def make_text(x,y,text,size, fill, font = "arial.ttf"):
    text = text
    font = ImageFont.truetype(font, size=size)
    idraw.multiline_text((x,y), text, font=font, fill = fill)

make_text(30, 20, defenition['word'], 45, fill='black', font = 'Bangers-Regular.ttf')


defenition['definition'] = '\n'.join(wrap(defenition['definition'], width=50))
make_text(30,80,defenition['definition'],20, fill='black', font = 'Gelasio-Regular.ttf')

make_text(30,200,defenition['example'], 20, fill='black', font = 'Gelasio-Regular.ttf')

croped = image.crop((0,0,500,270))


croped.show()
# croped.save('plant mom.png')
