import image_processing
from PIL import Image

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

shirtpath = 'C:\\Users\\stsha\\fithub\\backend\\tshirtnobg.png'
pantspath = 'C:\\Users\\stsha\\fithub\\backend\\pantsnobg.png'
shirtlen = int(image_processing.process_images('shirt'))
pantslen = int(image_processing.process_images('pants'))

resized_pic = (scale_action(shirtpath, scaling_factor(shirtlen, pantslen, shirtpath, pantspath)[0]))
resized_pic.save('C:\\Users\\stsha\\fithub\\backend\\shrink_file.png')