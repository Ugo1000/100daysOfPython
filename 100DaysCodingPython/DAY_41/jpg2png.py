#!/usr/bin/python3

import sys
from pathlib import Path
from PIL import Image

# Grab first and second arguments
str_pic_folder = sys.argv[1]
str_output_folder = sys.argv[2]


# Check is new exits , if not create
mypath = Path(str_output_folder)

if not mypath.exists():
    mypath.mkdir(parents=True)

# Loop through my_picture folder
pic_folder = Path(str_pic_folder)

for out_file in pic_folder.iterdir():
    # check if it's a file
    if out_file.is_file():

        # Open image
        img = Image.open(out_file)
        # Define output file path
        out_file_path = mypath / (out_file.stem + ".png")

        # Save image to output folder
        img.save(out_file_path)
        img.show()


# Convert images to png

# Save to the new folder
