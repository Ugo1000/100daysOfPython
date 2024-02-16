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
pic_folder = Path(str_output_folder)

for out_file in pic_folder.iterdir():
    img = Image.open(f"{pic_folder}, {out_file}")
    print(img)


# Convert images to png

# Save to the new folder
