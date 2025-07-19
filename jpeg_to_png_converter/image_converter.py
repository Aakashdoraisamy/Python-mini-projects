import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    clean_name = os.path.splitext(filename)[0]
    img_path = os.path.join(image_folder, filename)
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img = Image.open(img_path)
        img.save(f"{output_folder}/{clean_name}.png", "png")
        print(f"Converted {filename} to PNG and saved in {output_folder}")
