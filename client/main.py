import random
import uuid
from PIL import Image, ImageDraw
import time

def generate_random_image(img_counter ,width=128, height=128):
    rand_pixels = [random.randint(0, 255) for _ in range(width * height * 3)]
    rand_pixels_as_bytes = bytes(rand_pixels)
    text_and_filename = "img" + str(img_counter)

    random_image = Image.frombytes('RGB', (width, height), rand_pixels_as_bytes)

    draw_image = ImageDraw.Draw(random_image)
    draw_image.text(xy=(0, 0), text=text_and_filename, fill=(255, 255, 255))
    random_image.save('out/{file_name}.jpg'.format(file_name=text_and_filename))

    print('INFO : Saved \t' + str(img_counter) + '. \t image!')
    time.sleep(1)

# Generate 42 random images: 
for img_counter in range(100):
    generate_random_image(img_counter + 1)