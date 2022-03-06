from PIL import Image

im = Image.open('montage.png')

width, height = int(8.27 * 300), int(11.7 * 300) # A4 at 300dpi
a4im = Image.new('RGB',
                 (width, height),
                 (255, 255, 255, 0))  # White
a4im.paste(im, (0, 0), im)
a4im.paste(im, (1250, 0), im)
a4im.paste(im, (1250, 2200), im)
a4im.paste(im, (0, 2200), im)
a4im.paste(im, (625, 1100), im)
# a4im.paste(im, (1250, 0)) 
# a4im.paste(im, (2000, 0)) 
# a4im.paste(im, (1250, 0)) 
# a4im.paste(im, (1250, 0)) 
a4im.save('collage.pdf', 'PDF', quality=100)