# Import the Required Libraries
import sys
import os
from PIL import Image

# Grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]

# Check if converted_images folder exits, if not then create it
if not os.path.exists(directory):
    os.makedirs(directory)
    

# Loop through the image folder, convert images to png and save it the new converted_images folder
for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')