from PIL import Image

img = Image.open('image.jpg')
img.rotate(45).show()
