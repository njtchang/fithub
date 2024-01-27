from rembg import remove
from PIL import Image

input_path = 'C:\\Users\\stsha\\fithub\\backend\\tshirt.png'
output_path = 'C:\\Users\\stsha\\fithub\\backend\\tshirtnobg.png'

input = Image.open(input_path)
output = remove(input)

output.save(output_path)