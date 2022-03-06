import os
from PIL import Image, ImageDraw, ImageOps
import random


image_dir = os.path.abspath("png")
# list all files in directory
files = os.listdir(image_dir)
# get all PNGs
png_files = filter(lambda x: x.endswith(".png"), files)
# make file paths absolute
image_files = map(lambda x: os.sep.join([image_dir, x]), png_files)

image_files = []
for file in png_files:
    image_files.append(image_dir + '/' + file)


target_img = None

diameter = 1200


target_img = Image.new("RGBA", (diameter, diameter), (255, 255, 255, 0))
circle_img = ImageDraw.Draw(target_img)
circle_img.ellipse((0, 0, diameter-1, diameter-1), outline ='grey')

MAX_SIZE = (diameter/3, diameter/3)


montage_details = [ # top left corner coordinates, zoom, degree rotation
    (50, 200),
    (50, 600),
    (400, 0),
    (400, 400),
    (400, 800),
    (750, 200),
    (750, 600)
]

for n in range(len(image_files)):
    img = Image.open(image_files[n]).convert('RGBA')

    x = montage_details[n][0]
    y = montage_details[n][1]


    # we reduce the size to something between 0.6 to 0.9 times the original size
    zoom = random.randrange(60, 91)/100
    img.thumbnail((MAX_SIZE[0]*zoom, MAX_SIZE[1]*zoom))

    # rotate by random angle
    random_angle = random.randrange(360)
    im2 = img.rotate(random_angle, expand=1)
    width, height = im2.size

    # find new coordinates due resizing
    offset_x = int(x - (width - MAX_SIZE[0])/2)
    offset_y = int(y - (height - MAX_SIZE[0])/2)


    # paste the image at the correct position
    target_img.paste(   im2, 
                        (offset_x, offset_y), 
                        im2)


# save the collage
target_img.save("montage.png")
