from rembg import remove
from PIL import Image

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
def measure(box, pnglist, clothingtype):
    width = box[2] - box[0]
    height = box[3] - box[1]
    print(width, height)

    xmiddle = int(((width) // 2) + 1)
    if clothingtype == 'shirt':
        ymeasure = int((5 * height) // 6)
    if clothingtype == 'pants':
        ymeasure = int(height // 6)
    print(xmiddle, ymeasure)
    index = (((ymeasure - 1) * width) + xmiddle) - 1

    # for pixel in pnglist[index:]:
    #     if pixel == 0:
    #         half_len_index = pnglist.index(pixel)
    #         break

    for pixeli in range(len(pnglist))[index:]:
        if pnglist[pixeli] == 0:
            half_len_index = pixeli
            break
    
    print(index, half_len_index)
    item_len = (half_len_index - index) * 2
    return item_len

def main():
    piece = 'pants'
    if piece == 'shirt':
        pic_path = 'C:\\Users\\stsha\\fithub\\backend\\tshirt.png'
        output_path = 'C:\\Users\\stsha\\fithub\\backend\\tshirtnobg.png'
    if piece == 'pants':
        pic_path = 'C:\\Users\\stsha\\fithub\\backend\\pants.png'
        output_path = 'C:\\Users\\stsha\\fithub\\backend\\pantsnobg.png'
    nobg = removebg(pic_path)
    info = crop(nobg, output_path)
    length = measure(info[0], info[1], piece)
    return length

print(main())
