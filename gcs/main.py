from PIL import Image
import os

try:
    n = 1
    while True:
        while True:
            if os.path.isfile('R:/py-program/out/img' + str(n) + '.jpg'):
                print('INFO: Read\t' + str(n) + '.\tImage')
                break
        n += 1;
        
except KeyboardInterrupt:
    pass

