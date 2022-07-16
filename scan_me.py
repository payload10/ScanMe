import os
import os
import sys
from PIL import Image
import math
from PIL import ImageEnhance

def convert(path):
    input=path
    picture = Image.open(input)
    # output="D:\\code\\C-Project\\old\\{}_Compressed.jpg".format(input.split('\\')[-1].split('.')[0])
    output="6.jpg"
    picture.save(output, 
                    "JPEG", 
                    optimize = True, 
                    quality = 25)

