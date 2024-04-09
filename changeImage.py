#!/usr/bin/env python3

from PIL import Image
from os import listdir
from os.path import isfile, join

for item in listdir("./supplier-data/images"):
 if ".tiff" in item:
  im = Image.open(join("./supplier-data/images",item))
  new_im = im.convert("RGB").resize((600,400))
  new_im.save(join("./supplier-data/images/",item.replace(".tiff","")) + ".jpeg")