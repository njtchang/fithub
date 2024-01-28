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

def create_file(shirt_id, pants_id):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    shirtpath = str(os.path.join(current_directory, 'images', 'shirtnobg.png'))
    pantspath = str(os.path.join(current_directory, 'images', 'pantsnobg.png'))
    shirtlen = int(image_processing.process_images('shirt', shirt_id))
    pantslen = int(image_processing.process_images('pants', pants_id))

    if shirtlen > pantslen:
        resized_pic = (scale_action(shirtpath, scaling_factor(shirtlen, pantslen, shirtpath, pantspath)[0]))
        resized_pic.save(str(os.path.join(current_directory, 'images', 'shrink_shirt.png')))
        shrinkshirtpath = str(os.path.join(current_directory, 'images', 'shrink_shirt.png'))
        images = [Image.open(x) for x in [shrinkshirtpath, pantspath]]

    if pantslen > shirtlen:
        resized_pic = (scale_action(pantspath, scaling_factor(shirtlen, pantslen, shirtpath, pantspath)[0]))
        resized_pic.save(str(os.path.join(current_directory, 'images', 'shrink_pants.png')))
        shrinkpantspath = str(os.path.join(current_directory, 'images', 'shrink_pants.png'))
        images = [Image.open(x) for x in [shirtpath, shrinkpantspath]]

    widths, heights = zip(*(i.size for i in images))
    max_width = max(widths)
    total_height = sum(heights)
    finalpng = Image.new('RGBA', (max_width, total_height))
    y_offset = 0
    for im in images:
        x_offset = int((finalpng.width - im.width) // 2)
        finalpng.paste(im, (x_offset, y_offset))
        y_offset += images[0].height

    finalpath = str(os.path.join(current_directory, 'images', 'combo_outfit.png'))
    finalpng.save(finalpath)

    return(finalpng)