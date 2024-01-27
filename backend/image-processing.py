from rembg import remove
from PIL import Image

output_path = 'C:\\Users\\stsha\\fithub\\backend\\tshirtnobg.png'
shirt = True
pants = not shirt

#removes the background of the image
def removebg(input_path):
    input = Image.open(input_path)
    output = remove(input)
    return output

#crops out the extra transparent space and reduces the image to minimum dimensions
def crop(file, newpath):
    box_size = file.getbbox()
    output_crop = file.crop(box_size)
    output_crop.save(newpath)
    array = list(output_crop.getdata(3))
    return box_size, array

#finds point to measure clothing from 
def measure(box, pnglist):
    width = box[2] - box[0]
    height = box[3] - box[1]
    print(width, height)

    xmiddle = int(((width) // 2) + 1)
    if shirt:
        ymeasure = int((5 * height) // 6)
    if pants:
        ymeasure = int(height // 6)
    print(xmiddle, ymeasure)
    index = int((((ymeasure - 1) * width) + xmiddle) - 1)

    for pixel in pnglist[index:]:
        if pixel == 0:
            half_len_index = pnglist.index(pixel)
            break
    print(half_len_index, index)
    if shirt:
        len = (half_len_index - index) * 2
    if pants:
        len = (half_len_index - index) * 2
    return len

def main():
    pic_path = 'C:\\Users\\stsha\\fithub\\backend\\tshirt.png'
    output_path = 'C:\\Users\\stsha\\fithub\\backend\\tshirtnobg.png'
    nobg = removebg(pic_path)
    info = crop(nobg, output_path)
    length = measure(info[0], info[1])
    return length

print(main())
