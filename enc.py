from PIL import Image 
from math import sqrt, ceil
import binascii

def file_to_image(input_file, output_image):
    with open(input_file, 'rb') as file:
        data = file.read()
    data = binascii.hexlify(data).decode('utf-8')
    #print(data, len(data))
    data_size_in_bits = len(data)
    width = height = ceil(sqrt(data_size_in_bits))
    image = Image.new('1', (width, height))
    pixel_index= 0
    for bit in data:
        x = pixel_index % width 
        y = pixel_index // width 
        pixel_value = int(bit, 16)
        #print(pixel_value)
        image.putpixel((x, y), pixel_value)
        pixel_index += 1
    image.save(output_image)
    
def image_to_file(input_image, output_file):
    image = Image.open(input_image)
    pixels = []
    for y in range(image.height):
        for x in range(image.width):
            pixel_value = image.getpixel((x, y))
            #pixel_value = 1 if pixel_value > 0 else 0
            pixels.append(format(pixel_value, 'x'))
    # data = bytearray()
    # current_byte = 0
    
    # for i, pixel in enumerate(pixels):
    #     if i == 107*8 - 1:
    #         break
    #     current_byte = (current_byte << 1) | pixel 
    #     if (i+1)%8 == 0:
    #         try:
    #             data.append(current_byte)
    #             current_byte = 0 
    #         except Exception as e:
    #             print('failed because i is', i, ' and current_byte is', current_byte, ' and pixel is', pixel)
    #             raise e
    binary_data = binascii.unhexlify(''.join(pixels))
    with open(output_file, 'wb') as file:
        file.write(binary_data)

file_to_image('play.js', 'output1.png')
image_to_file('output1.png', 'output1.js')