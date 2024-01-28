import image_processing
from PIL import Image, ImageDraw
import os
from pathlib import Path

def scaling_factor(lenshirt, lenpants, shirtfile, pantsfile):
    if lenshirt > lenpants:
        return (lenpants / lenshirt), shirtfile
    if lenpants > lenshirt:
        return (lenshirt / lenpants), pantsfile
    else:
        return 1
    
def scale_action(filepath, factor):
    img = Image.open(filepath)
    width = img.width
    height = img.height
    new_width = int(width * factor)
    new_height = int(height * factor)
    newsize = (new_width, new_height)
    img = img.resize(newsize)
    return img

def create_file():
    shirtpath = 'C:\\Users\\stsha\\fithub\\backend\\tshirtnobg.png'
    pantspath = 'C:\\Users\\stsha\\fithub\\backend\\pantsnobg.png'
    shirtlen = int(image_processing.process_images('shirt'))
    pantslen = int(image_processing.process_images('pants'))

    if shirtlen > pantslen:
        resized_pic = (scale_action(shirtpath, scaling_factor(shirtlen, pantslen, shirtpath, pantspath)[0]))
        resized_pic.save('C:\\Users\\stsha\\fithub\\backend\\shrink_shirt.png')
        final_shirt = resized_pic
        final_pants = Image.open(pantspath)
        images = [Image.open(x) for x in ['C:\\Users\\stsha\\fithub\\backend\\shrink_shirt.png', pantspath]]
        # final_shirtpath = Path(resized_pic)
        # final_pantspath = Path(pantspath)
    if pantslen > shirtlen:
        resized_pic = (scale_action(pantspath, scaling_factor(shirtlen, pantslen, shirtpath, pantspath)[0]))
        resized_pic.save('C:\\Users\\stsha\\fithub\\backend\\shrink_pants.png')
        final_shirt = Image.open(shirtpath)
        final_pants = resized_pic
        images = [Image.open(x) for x in [shirtpath, 'C:\\Users\\stsha\\fithub\\backend\\shrink_pants.png']]
        # final_shirtpath = Path(shirtpath)
        # final_pantspath = Path(pantspath)

    # final_shirt = Image.open(final_shirtpath)
    # final_pants = Image.open(final_pantspath)
    # canvas_height = (final_shirt.height + final_pants.height)
    # canvas_width = max([final_shirt.width, final_pants.width])
    # combo_canvas = Image.new('RGBA', (canvas_width, canvas_height), (0, 0, 0, 0))

    # combo_canvas.save('C:\\Users\\stsha\\fithub\\backend\\combo_outfit.png')

    # background = Image.open('C:\\Users\\stsha\\fithub\\backend\\combo_outfit.png')
    widths, heights = zip(*(i.size for i in images))
    max_width = max(widths)
    total_height = sum(heights)
    finalpng = Image.new('RGBA', (max_width, total_height))
    y_offset = 0
    for im in images:
        x_offset = int((finalpng.width - im.width) // 2)
        finalpng.paste(im, (x_offset, y_offset))
        y_offset += images[0].height

    finalpng.save('combo_outfit.png')
        
    # background.paste(final_shirt, (0, 0), mask = final_shirt)
    # background.paste(final_pants, (0, 0), mask = final_pants)

create_file()
