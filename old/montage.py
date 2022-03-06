import os
from PIL import Image, ImageDraw

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
n_targets = 0
collage_saved = False



target_img = Image.new("RGBA", (900, 900), (255, 255, 255))
circle_img = ImageDraw.Draw(target_img)
circle_img.ellipse((0, 0, 900, 900), outline ='grey')

montage_details = [
    ((100, 170), 0.7, 51),
    ((90, 450), 0.8, 103),
    ((300, 50), 0.7, 154),
    ((300, 300), 1.0, 206),
    ((300, 575), 0.8, 257),
    ((525, 150), 0.7, 309),
    ((550, 450), 0.6, 0)
]

for n in range(len(image_files)):
    img = Image.open(image_files[n]).convert('RGBA')

    x = montage_details[n][0][0]
    y = montage_details[n][0][1]
    zoom = montage_details[n][1]
    rotation_angle = montage_details[n][2]
    img.thumbnail((int(300*zoom), int(300*zoom)))
    im2 = img.rotate(rotation_angle, expand=1)
    width, height = im2.size

    # paste the image at the correct position
    target_img.paste(   im2, 
                        # (x, y), 
                        (int(x+(x-width)/4), int(y+(y-height)/4)), 
                        im2)

    # if (n + 1) % 3 == 0 and target_img is not None:
    #     # save a finished 8x8 collage
    #     target_img.save("{0:04}.png".format(n_targets))
    #     collage_saved = True

# save the last collage
if not collage_saved:
    target_img.save("montage.png")
