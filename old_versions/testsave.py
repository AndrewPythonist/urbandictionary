from PIL import Image
import io


# imageB = open('cards/420.png', 'rb')
# print(type(imageB))

image = Image.new('RGB', (500,500), 'red')
byte_io = io.BytesIO()
image.save(byte_io, format='png')
byte_io.seek(0)
# print(byte_io)
open(byte_io, 'rb')