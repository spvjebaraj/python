import sys
import os
from PIL import Image


# grab first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder)
print(output_folder)

# check if new folder exists, else create new one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    if filename == '.DS_Store':
        continue

    # split the filename
    without_extension = os.path.splitext(filename)[0]
    img = Image.open(f'{image_folder}{filename}')
    img.save(f'{output_folder}{without_extension}.png', "png")
    print("all done")
