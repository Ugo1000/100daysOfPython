from PIL import Image
import sys
import os


# grab the first and second arguments
image_folder = sys.argv[1]
out_put = sys.argv[2]


# check if they exits
if not os.path.exists(out_put):
    os.makedirs(out_put)
