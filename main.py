from PIL import Image
from colorit import background, init_colorit

init_colorit() # clear the terminal
depth = int(input('enter a depth'))

image = Image.open('Image path')

image = image.resize((depth,depth)) # Enter a size 
for y in range(image.size[1]):
    for x in range(image.size[0]):
        print(background(' ',image.getpixel((x,y))),end = '')
    print()
