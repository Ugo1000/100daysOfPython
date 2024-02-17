#!/usr/bin/python3

from PIL import Image
import sys
import os


# grab the first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# check if they exits
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(image_folder):
    # open image

    img = Image.open(f'{image_folder}{filename}')
    # remove the extension
    print(type(img))
    clean_name = os.path.splitext(filename)[0]
    # save the image to the new folder
    img.save(f'{output_folder}{clean_name}.png', format="PNG")
    print("All Done..")

    img = Image.open(f'{image_folder}{filename}')  # open the image
    clean_name = os.path.splitext(filename)[0]  # remove the extension
    # save the image to the new folder
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')
