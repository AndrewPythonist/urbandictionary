from PIL import Image, ImageDraw
from random import randint as rint

def random_gradient():
    img = Image.new("RGB", (500,500), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    r,g,b = rint(0,255), rint(0,255), rint(0,255)
    dr = (rint(0,255) - r)/500.
    dg = (rint(0,255) - g)/500.
    db = (rint(0,255) - b)/500.
    for i in range(500):
        r,g,b = r+dr, g+dg, b+db
        draw.line((i,0,i,500), fill=(int(r),int(g),int(b)))

    return img

if __name__ == '__main__':
    random_gradient().show()