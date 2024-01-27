from rembg import remove
from PIL import Image

input_path = 'C:\\Users\\stsha\\fithub\\backend\\tshirt.png'
output_path = 'C:\\Users\\stsha\\fithub\\backend\\tshirtnobg.png'

input = Image.open(input_path)
output = remove(input)

output_crop = output.crop(output.getbbox())
output_crop.save(output_path)
array = list(output_crop.getdata(3))

output_crop.save(output_path)

print(array)
